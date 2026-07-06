import torch
import torch.optim as optim

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)