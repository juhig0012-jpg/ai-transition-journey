# Import the PyTorch library
import torch

# Import the neural network module
import torch.nn as nn


# ----------------------------------------
# Create a Neural Network using nn.Sequential
# ----------------------------------------
#
# nn.Sequential automatically connects the layers
# in the order they are written.
#
# Data Flow:
#
# Input (2 Features)
#        │
#        ▼
# Linear (2 → 4)
#        │
#        ▼
# ReLU Activation
#        │
#        ▼
# Linear (4 → 1)
#        │
#        ▼
# Final Output
#
model = nn.Sequential(

    # First Fully Connected Layer
    #
    # Input Features = 2
    # Output Features = 4
    #
    # Example:
    # Input:
    # [x1, x2]
    #
    # Output:
    # [h1, h2, h3, h4]
    nn.Linear(2, 4),

    # ReLU Activation Function
    #
    # Formula:
    # ReLU(x) = max(0, x)
    #
    # Example:
    #
    # Before ReLU
    # [-2, 3, -1, 5]
    #
    # After ReLU
    # [0, 3, 0, 5]
    #
    # It removes negative values and
    # introduces non-linearity.
    nn.ReLU(),

    # Second Fully Connected Layer
    #
    # Input Features = 4
    # Output Features = 1
    #
    # Example:
    # [h1, h2, h3, h4]
    #
    # Output:
    # [prediction]
    nn.Linear(4, 1)
)


# ----------------------------------------
# Create Sample Input
# ----------------------------------------
#
# Shape = (1,2)
#
# 1 = One sample
# 2 = Two input features
#
# Sample:
#
# Feature 1 = 1.0
# Feature 2 = 2.0
#
x = torch.tensor([[1.0, 2.0]])


# ----------------------------------------
# Forward Pass
# ----------------------------------------
#
# This automatically performs:
#
# Step 1:
# x → Linear(2→4)
#
# Step 2:
# Output → ReLU
#
# Step 3:
# Output → Linear(4→1)
#
# Final Prediction is returned.
#
output = model(x)


# Print the predicted output
print(output)