import os
import ast
import torch
from torch.utils.data.dataset import Dataset

class CellData(Dataset):
    def __init__(self, root, filter_str='.txt', single_mode=False):

        assert isinstance(filter_str, str), "invalid `filter_str` format."
        self.filter_str = filter_str if single_mode else '.txt'

        self.data = self.get_data(root)

    def get_data(self, folder_path):
        all_data = []

        for filename in os.listdir(folder_path):
            if filename.endswith(self.filter_str):
                file_path = os.path.join(folder_path, filename)

                with open(file_path, 'r') as file:
                    data_str = file.read()

                data_list = ast.literal_eval(data_str)

                all_data.extend(data_list)
        data = torch.tensor(all_data, dtype=torch.float32)

        return data

    def __getitem__(self, index):
        vector = self.data[index]
        labels = vector[6:]
        inputs = vector[:6]
        return inputs, labels
    
    def __len__(self):
        return len(self.data)