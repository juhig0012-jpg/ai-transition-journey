# Import PyTorch library
import torch

# Import Dataset and DataLoader classes
from torch.utils.data import Dataset, DataLoader

# Import Neural Network module
import torch.nn as nn


# =====================================================
# Step 1: Create Custom Dataset
# =====================================================

# Every custom dataset should inherit from Dataset
class StudentDataset(Dataset):

    # Constructor
    def __init__(self):

        # Input Feature (Hours Studied)
        # Shape = (6,1)
        self.X = torch.tensor([
            [1.0],
            [2.0],
            [3.0],
            [4.0],
            [5.0],
            [6.0]
        ])

        # Target Values (Marks)
        # Shape = (6,1)
        self.y = torch.tensor([
            [15.0],
            [30.0],
            [45.0],
            [60.0],
            [75.0],
            [90.0]
        ])

    # Returns total number of samples
    def __len__(self):
        return len(self.X)

    # Returns one sample at the given index
    def __getitem__(self, index):
        return self.X[index], self.y[index]


# =====================================================
# Step 2: Create Dataset Object
# =====================================================

dataset = StudentDataset()


# =====================================================
# Step 3: Create DataLoader
# =====================================================

# DataLoader automatically creates mini-batches
loader = DataLoader(
    dataset,
    batch_size=3,   # 3 samples per batch
    shuffle=True    # Shuffle data every epoch
)


# =====================================================
# Step 4: Print Batches
# =====================================================

print("Batches:\n")

# Iterate through DataLoader
for batch_X, batch_y in loader:

    print("Hours:")
    print(batch_X)

    print("Marks:")
    print(batch_y)

    print("-" * 40)


# =====================================================
# Step 5: Create Linear Regression Model
# =====================================================

# Model:
# y = wx + b
model = nn.Linear(1, 1)


# =====================================================
# Step 6: Loss Function
# =====================================================

# Mean Squared Error Loss
criterion = nn.MSELoss()


# =====================================================
# Step 7: Optimizer
# =====================================================

# Stochastic Gradient Descent
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)


# =====================================================
# Step 8: Training Loop
# =====================================================

epochs = 100

for epoch in range(epochs):

    # Iterate through every mini-batch
    for batch_X, batch_y in loader:

        # Forward Pass
        predictions = model(batch_X)

        # Calculate loss
        loss = criterion(predictions, batch_y)

        # Clear previous gradients
        optimizer.zero_grad()

        # Compute gradients
        loss.backward()

        # Update weights
        optimizer.step()

    # Print loss every 10 epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1:3d} | Loss = {loss.item():.4f}")


# =====================================================
# Step 9: Test Model
# =====================================================

print("\nTesting Model")

# Disable gradient calculation during testing
with torch.no_grad():

    # Predict marks for 7 hours of study
    test = torch.tensor([[7.0]])

    prediction = model(test)

    print(f"Hours = 7")
    print(f"Predicted Marks = {prediction.item():.2f}")