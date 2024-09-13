import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from anode.models import ODENet
from anode.train import Trainer
from experiments.dataloader import CellData
import argparse


parser = argparse.ArgumentParser(description="ML STA Training")
parser.add_argument("--train-dir", type=str, default='/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Ours/Dataset/train_data', help="train dir root")
parser.add_argument("--test-dir", type=str, default='/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Ours/Dataset/test_data', help="test dir root")
parser.add_argument("--save-dir", type=str, default='results/ANODE', help="save dir")
parser.add_argument("--epoch", type=int, default=250, help="training epoch")
parser.add_argument("--print-freq", type=int, default=50, help="printing frequency")
parser.add_argument("--eval-epoch", type=int, default=5, help="evaluating frequency")
parser.add_argument("--lr", type=float, default=5e-3, help="learning rate")
parser.add_argument("--input-dim", type=int, default=6, help="input data dim")
parser.add_argument("--hidden-dim", type=int, default=64, help="hidden dim")
parser.add_argument("--bsz", type=int, default=64, help="training batch size")
parser.add_argument("--eval-bsz", type=int, default=64, help="evaluate batch size")
args = parser.parse_args()


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# dataset
train_dataset, test_dataset = CellData(args.train_dir), CellData(args.test_dir)

train_loader = DataLoader(train_dataset, batch_size=args.bsz, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=args.eval_bsz, shuffle=False)

model = ODENet(device, args.input_dim, args.hidden_dim,
               time_dependent=False, non_linearity='relu').to(device)

optimizer = optim.Adam(model.parameters(), lr=args.lr)

# Train
model.train()
trainer = Trainer(model, optimizer, device,
                  print_freq=args.print_freq, save_dir=(f'{args.save_dir}_{args.epoch}', 0),
                  test_loader=test_loader, evaluate_epoch=args.eval_epoch,)
trainer.train(train_loader, args.epoch)
torch.save(model.state_dict(), f'{args.save_dir}_{args.epoch}/model.pkl')
