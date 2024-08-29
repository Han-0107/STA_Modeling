import torch
import ast
import os
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from anode.models import ODENet
from anode.train import Trainer
from anode.test import Tester
from experiments.dataloader import CellData

device = torch.device('cpu')

data_dim = 6
hidden_dim = 20

# 指定文件夹路径
folder_path = '/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Ours/Dataset/'

# 初始化一个空列表来存储所有文件的数据
all_data = []

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # 读取每个txt文件的内容
        with open(file_path, 'r') as file:
            data_str = file.read()
        
        # 解析文件内容为嵌套列表
        data_list = ast.literal_eval(data_str)
        
        # 将数据添加到all_data列表中
        all_data.extend(data_list)

# 将所有数据转换为torch.tensor
data = torch.tensor(all_data, dtype=torch.float32)

dataset = CellData(data)
train_loader = DataLoader(dataset, batch_size=5, shuffle=True)
test_loader = DataLoader(dataset, batch_size=5, shuffle=True)

model = ODENet(device, data_dim, hidden_dim, time_dependent=False, non_linearity='relu')

optimizer = optim.Adam(model.parameters(), lr=0.005)

train_epochs = 200
test_epochs = 10

# Train the model
model.train()
trainer = Trainer(model, optimizer, device, print_freq=50)
trainer.train(train_loader, train_epochs)

# Test the model
model.eval()
tester = Tester(model, device, print_freq=50)
tester.test(test_loader, test_epochs)
