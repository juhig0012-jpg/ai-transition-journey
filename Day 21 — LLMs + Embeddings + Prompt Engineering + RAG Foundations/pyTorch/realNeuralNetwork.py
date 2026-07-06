import torch
import torch.nn as nn

# Input and target
X = torch.tensor([[1.0], [2.0], [3.0]])
y = torch.tensor([[2.0], [4.0], [6.0]])

# Model
model = nn.Linear(1, 1)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(5):
    prediction = model(X)          # Forward pass
    loss = criterion(prediction, y)

    optimizer.zero_grad()          # Clear previous gradients
    loss.backward()                # Compute new gradients
    optimizer.step()               # Update weights

    print(f"Epoch {epoch + 1}: Loss = {loss.item():.4f}")