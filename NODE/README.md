# Time Prediction through Neural ODE

## Data Format

Now, we represent the simulation result of a cell by a vector. The **type** of cell is represented by the one-hot code composed of the first three elements of the vector. The **voltage**, **load capacitance** and **input transition time** of the cell are in the 4th and 5th bits respectively. The **time propagation of high to low** (tphl) and **time propagation of low to high** (tplh) obtained by hspice simulation are stored in the last two bits respectively.

## Train and Test

This repo refers to https://github.com/EmilienDupont/augmented-neural-odes. The Dataset for Neural ODE model is saved in `./Spice/Libs/Dataset`.

1. Run `python ./NODE/train.py`, the log of training will be stored in `./NODE/log`. You can examine them in [TensorBoard](https://www.tensorflow.org/tensorboard).
2. Run `python ./NODE/test.py`, you can choose a model manually.

After training, each model will record the changes of its loss and MAPE during training and store them in `./NODE/models/ANODE_xxx`. Like these:

![Loss & Iterations](NODE/models/ANODE_300/training_loss_epoch_300.png)

![MAPE & Iterations](NODE/models/ANODE_300/training_mape_epoch_300.png)
