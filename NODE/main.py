import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from anode.models import ODENet
from anode.training import Trainer
from experiments.dataloader import CellData

device = torch.device('cpu')

data_dim = 6
hidden_dim = 16

data = torch.tensor([
    [0, 0, 1, 1.0, 2.0, 3.0, 4.0, 5.0],
    [0, 1, 0, 6.0, 7.0, 8.0, 9.0, 10.0],
    [0, 1, 1, 11.0, 12.0, 13.0, 14.0, 15.0]
])

dataset = CellData(data)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

model = ODENet(device, data_dim, hidden_dim, time_dependent=False, non_linearity='relu')

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 20

trainer = Trainer(model, optimizer, device)
trainer.train(dataloader, num_epochs)
