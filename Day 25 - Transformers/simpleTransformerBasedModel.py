import torch
import torch.nn as nn

class MiniTransformer(nn.Module):

    def __init__(self):

        super().__init__()

        self.embedding = nn.Embedding(1000,64)

        self.attention = nn.MultiheadAttention(
            embed_dim=64,
            num_heads=8,
            batch_first=True
        )

        self.fc = nn.Linear(64,2)

    def forward(self,x):

        x = self.embedding(x)

        x, _ = self.attention(x,x,x)

        x = x.mean(dim=1)

        return self.fc(x)

model = MiniTransformer()

sample = torch.randint(0,1000,(4,20))

output = model(sample)

print(output.shape)