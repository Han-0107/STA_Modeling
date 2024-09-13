import json
import torch
import torch.nn as nn
from numpy import mean


class Tester():
    """Class used to test ODENets, ConvODENets and ResNets.

    Parameters
    ----------
    model : one of models.ODENet, conv_models.ConvODENet, discrete_models.ResNet

    device : torch.device

    classification : bool
        If True, tests a classification model with cross entropy loss,
        otherwise tests a regression model with Huber loss.

    print_freq : int
        Frequency with which to print information (loss, nfes etc).

    record_freq : int
        Frequency with which to record information (loss, nfes etc).

    verbose : bool
        If True prints information (loss, nfes etc) during testing.

    save_dir : None or tuple of string and string
        If not None, saves losses and nfes (for ode models) to directory
        specified by the first string with id specified by the second string.
        This is useful for testing models when underflow in the time step or
        excessively large NFEs may occur.
    """
    def __init__(self, model, device, classification=False,
                 print_freq=10, record_freq=10, verbose=True, save_dir=None):
        self.model = model
        self.classification = classification
        self.device = device
        if self.classification:
            self.loss_func = nn.CrossEntropyLoss()
        else:
            self.loss_func = nn.SmoothL1Loss()
        self.print_freq = print_freq
        self.record_freq = record_freq
        self.steps = 0
        self.save_dir = save_dir
        self.verbose = verbose

        self.histories = {'loss_history': [], 'nfe_history': [],
                          'bnfe_history': [], 'total_nfe_history': [],
                          'epoch_loss_history': [], 'epoch_nfe_history': [],
                          'epoch_bnfe_history': [], 'epoch_total_nfe_history': []}
        self.buffer = {'loss': [], 'nfe': [], 'bnfe': [], 'total_nfe': []}

        # Only resnets have a number of layers attribute
        self.is_resnet = hasattr(self.model, 'num_layers')

    def test(self, data_loader, num_epochs):
        """Tests model on data in data_loader for num_epochs.

        Parameters
        ----------
        data_loader : torch.utils.data.DataLoader

        num_epochs : int
        """
        for epoch in range(num_epochs):
            if self.verbose:
                print("\n\033[1;32mTest Epoch {}\033[0m".format(epoch + 1))
            avg_loss = self._test_epoch(data_loader, epoch)
            print("epoch loss: {:.4f}".format(avg_loss))

    def _test_epoch(self, data_loader, epoch):
        """Tests model for an epoch.

        Parameters
        ----------
        data_loader : torch.utils.data.DataLoader
        """
        epoch_loss = 0.
        epoch_nfes = 0
        epoch_backward_nfes = 0
        with torch.no_grad():
            for i, (x_batch, y_batch) in enumerate(data_loader):

                x_batch = x_batch.to(self.device)
                y_batch = y_batch.to(self.device)

                y_pred = self.model(x_batch)

                # ResNets do not have an NFE attribute
                if not self.is_resnet:
                    iteration_nfes = self._get_and_reset_nfes()
                    epoch_nfes += iteration_nfes

                loss = self.loss_func(y_pred, y_batch)
                epoch_loss += loss.item()

                if not self.is_resnet:
                    iteration_backward_nfes = self._get_and_reset_nfes()
                    epoch_backward_nfes += iteration_backward_nfes

                if i % self.print_freq == 0:
                    if self.verbose:
                        # print("Iteration {}/{}".format(i, len(data_loader)))
                        # print("Loss: {:.4f}".format(loss.item()))
                        error = self.calculate_error(y_pred, y_batch)
                        print("\nError: ", error)
                        print("Prediction: ", y_pred)
                        print("Truth: ", y_batch)
                        # print("Loss: {:.3f}".format(loss.item()))
                        # if not self.is_resnet:
                        #     print("NFE: {}".format(iteration_nfes))
                        #     print("BNFE: {}".format(iteration_backward_nfes))
                        #     print("Total NFE: {}".format(iteration_nfes + iteration_backward_nfes))

                # Record information in buffer at every iteration
                self.buffer['loss'].append(loss.item())
                if not self.is_resnet:
                    self.buffer['nfe'].append(iteration_nfes)
                    self.buffer['bnfe'].append(iteration_backward_nfes)
                    self.buffer['total_nfe'].append(iteration_nfes + iteration_backward_nfes)

                # At every record_freq iteration, record mean loss, nfes, bnfes and
                # so on and clear buffer
                if self.steps % self.record_freq == 0:
                    self.histories['loss_history'].append(mean(self.buffer['loss']))

                    if not self.is_resnet:
                        self.histories['nfe_history'].append(mean(self.buffer['nfe']))
                        self.histories['bnfe_history'].append(mean(self.buffer['bnfe']))
                        self.histories['total_nfe_history'].append(mean(self.buffer['total_nfe']))

                    # Clear buffer
                    self.buffer['loss'] = []
                    self.buffer['nfe'] = []
                    self.buffer['bnfe'] = []
                    self.buffer['total_nfe'] = []

                    # Save information in directory
                    if self.save_dir is not None:
                        dir, id = self.save_dir
                        with open('{}/losses{}.json'.format(dir, id), 'w') as f:
                            json.dump(self.histories['loss_history'], f)
                        if not self.is_resnet:
                            with open('{}/nfes{}.json'.format(dir, id), 'w') as f:
                                json.dump(self.histories['nfe_history'], f)
                            with open('{}/bnfes{}.json'.format(dir, id), 'w') as f:
                                json.dump(self.histories['bnfe_history'], f)
                            with open('{}/total_nfes{}.json'.format(dir, id), 'w') as f:
                                json.dump(self.histories['total_nfe_history'], f)

                self.steps += 1

        # Record epoch mean information
        self.histories['epoch_loss_history'].append(epoch_loss / len(data_loader))
        if not self.is_resnet:
            self.histories['epoch_nfe_history'].append(float(epoch_nfes) / len(data_loader))
            self.histories['epoch_bnfe_history'].append(float(epoch_backward_nfes) / len(data_loader))
            self.histories['epoch_total_nfe_history'].append(float(epoch_backward_nfes + epoch_nfes) / len(data_loader))

        return epoch_loss / len(data_loader)

    def _get_and_reset_nfes(self):
        """Returns and resets the number of function evaluations for model."""
        if hasattr(self.model, 'odeblock'):  # If we are using ODENet
            iteration_nfes = self.model.odeblock.odefunc.nfe
            # Set nfe count to 0 before backward pass, so we can
            # also measure backwards nfes
            self.model.odeblock.odefunc.nfe = 0
        else:  # If we are using ODEBlock
            iteration_nfes = self.model.odefunc.nfe
            self.model.odefunc.nfe = 0
        return iteration_nfes

    def calculate_error(self, predictions, truths):
        absolute_errors = torch.abs(predictions - truths)
        relative_errors = absolute_errors / torch.abs(truths)
        error = relative_errors.mean().item()
        return round(error, 4)