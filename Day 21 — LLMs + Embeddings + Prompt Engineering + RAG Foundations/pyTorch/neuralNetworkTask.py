# ---------------------------------------------------------
# Import PyTorch
# ---------------------------------------------------------
import torch

# Import the neural network module
import torch.nn as nn


# ---------------------------------------------------------
# Build the Neural Network using nn.Sequential
# ---------------------------------------------------------
#
# Network Architecture:
#
# Input (3)
#      │
#      ▼
# Linear (3 → 8)
#      │
#      ▼
# ReLU
#      │
#      ▼
# Linear (8 → 4)
#      │
#      ▼
# ReLU
#      │
#      ▼
# Linear (4 → 2)
#      │
#      ▼
# Output (2)
#
# nn.Sequential automatically connects each layer
# in the order they are listed.
#
model = nn.Sequential(

    # First Fully Connected Layer
    #
    # Input Features = 3
    # Output Features = 8
    nn.Linear(3, 8),

    # ReLU Activation Function
    # Replaces negative values with 0
    nn.ReLU(),

    # Second Fully Connected Layer
    #
    # Input Features = 8
    # Output Features = 4
    nn.Linear(8, 4),

    # Another ReLU Activation
    nn.ReLU(),

    # Final Fully Connected Layer
    #
    # Input Features = 4
    # Output Features = 2
    nn.Linear(4, 2)
)


# ---------------------------------------------------------
# Print the Model Architecture
# ---------------------------------------------------------
#
# This shows every layer in the network.
#
print("Model Architecture:")
print(model)


# ---------------------------------------------------------
# Create Sample Input
# ---------------------------------------------------------
#
# Shape = (1,3)
#
# 1 = Number of samples
# 3 = Number of input features
#
x = torch.tensor([[1.0, 2.0, 3.0]])


# ---------------------------------------------------------
# Forward Pass
# ---------------------------------------------------------
#
# Data Flow:
#
# Input
#   ↓
# Linear(3→8)
#   ↓
# ReLU
#   ↓
# Linear(8→4)
#   ↓
# ReLU
#   ↓
# Linear(4→2)
#   ↓
# Output
#
output = model(x)


# ---------------------------------------------------------
# Print the Final Output
# ---------------------------------------------------------
#
# Output Shape = (1,2)
#
print("\nNetwork Output:")
print(output)


# ---------------------------------------------------------
# Calculate Total Trainable Parameters
# ---------------------------------------------------------
#
# model.parameters() returns all weights and biases.
#
# p.numel() returns the total number of values in
# each weight/bias tensor.
#
# p.requires_grad ensures only trainable parameters
# are counted.
#
total_params = sum(
    p.numel() for p in model.parameters()
    if p.requires_grad
)

print("\nTotal Trainable Parameters:", total_params)