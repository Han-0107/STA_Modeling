import numpy as np
import torch
import ast
import os
from torch.utils.data import DataLoader
from anode.models import ODENet
from experiments.dataloader import CellData
import argparse
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def mape(y_pred, y_true):

    return torch.abs((y_true - y_pred) / y_true)

def tester(model, data_loader, device=None):

    model.eval()
    total_mape = [0., 0.]
    pred_data = []
    with torch.no_grad():
        for i, (x_batch, y_batch) in enumerate(data_loader):
            x_batch = x_batch.to(device)
            y_batch = y_batch.to(device)
            y_pred = model(x_batch)

            batch_mape = mape(y_pred, y_batch)
            total_mape = [t_0 + t_1 for t_0, t_1 in zip(total_mape, batch_mape)]

            pred_data.append(x_batch.tolist()[0]+(y_pred.tolist()[0]))

    avg_mape = [e/len(data_loader.dataset) * 100 for e in total_mape[0]]

    bold_green = "\033[1;32m"
    reset = "\033[0m"

    print(f"{bold_green}tpHL MAPE{reset}: {avg_mape[0].item():.4f} %")
    print(f"{bold_green}tpLH MAPE{reset}: {avg_mape[1].item():.4f} %")

    return avg_mape


def load_model(model, model_filepath, device):

    model.load_state_dict(torch.load(model_filepath, map_location=device))

    return model

def main():

    parser = argparse.ArgumentParser(description="ML STA test")
    parser.add_argument("--test-dir", type=str, default='/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Ours/Dataset/test', help="test dir root")
    parser.add_argument("--filter-str", type=str, default='.txt', help="filter string")
    parser.add_argument("--single-mode", type=bool, default=False, help="whether to test the single test file")
    parser.add_argument("--input-dim", type=int, default=6, help="input data dim")
    parser.add_argument("--hidden-dim", type=int, default=64, help="hidden dim")
    parser.add_argument("--pkl-path", type=str, default='/data/yaohuihan/Research/STA_Modeling/NODE/models/ANODE_250/model.pkl', help="pkl file path")
    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    dataset = CellData(args.test_dir, filter_str=args.filter_str, single_mode=args.single_mode)
    test_loader = DataLoader(dataset, batch_size=1, shuffle=False)

    model = ODENet(device, args.input_dim, args.hidden_dim, time_dependent=False, non_linearity='relu').to(device)
    model = load_model(model, args.pkl_path, device=device)

    tester(model, test_loader, device=device)


if __name__ == "__main__":
    main()