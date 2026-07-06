# ---------------------------------------------------------
# Import PyTorch
# ---------------------------------------------------------
import torch

# Import PyTorch Neural Network module
import torch.nn as nn


# ---------------------------------------------------------
# Create a Simple Linear Model
# ---------------------------------------------------------
#
# nn.Linear(1,1) means:
#
# Input Features  = 1
# Output Features = 1
#
# Mathematical Equation:
#
# y = wx + b
#
# where:
# w = weight (learned during training)
# b = bias (learned during training)
#
# Initially, PyTorch assigns random values to w and b.
#
model = nn.Linear(1, 1)


# ---------------------------------------------------------
# Define the Loss Function
# ---------------------------------------------------------
#
# MSELoss = Mean Squared Error Loss
#
# Formula:
#
# Loss = ((Prediction - Actual)^2).mean()
#
# It measures how far the predictions are
# from the actual target values.
#
criterion = nn.MSELoss()


# ---------------------------------------------------------
# Create Input Data (Features)
# ---------------------------------------------------------
#
# Shape = (3,1)
#
# There are 3 training samples.
#
# Sample 1 → x = 1
# Sample 2 → x = 2
# Sample 3 → x = 3
#
x = torch.tensor([[1.0],
                  [2.0],
                  [3.0]])


# ---------------------------------------------------------
# Create Target Output (Labels)
# ---------------------------------------------------------
#
# Desired relationship:
#
# y = 2x
#
# x=1 → y=2
# x=2 → y=4
# x=3 → y=6
#
y = torch.tensor([[2.0],
                  [4.0],
                  [6.0]])


# ---------------------------------------------------------
# Forward Pass
# ---------------------------------------------------------
#
# Pass the input through the model.
#
# The model calculates:
#
# prediction = (weight × x) + bias
#
# Since weight and bias are randomly initialized,
# the predictions will not match the target values.
#
prediction = model(x)


# ---------------------------------------------------------
# Calculate the Loss
# ---------------------------------------------------------
#
# Compare:
#
# Prediction
#      VS
# Actual Target
#
# MSELoss computes:
#
# ((prediction - y)^2).mean()
#
# A smaller loss means the predictions are closer
# to the correct values.
#
loss = criterion(prediction, y)


# ---------------------------------------------------------
# Print the Loss
# ---------------------------------------------------------
#
# Example Output:
#
# tensor(12.3456, grad_fn=<MseLossBackward0>)
#
# The exact value will be different every time
# because the model starts with random weights.
#
print(loss)