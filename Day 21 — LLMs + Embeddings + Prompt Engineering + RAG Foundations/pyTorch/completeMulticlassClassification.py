# ---------------------------------------------------------
# Import PyTorch
# ---------------------------------------------------------
import torch

# Import the neural network module
import torch.nn as nn


# ---------------------------------------------------------
# Create a Linear Model
# ---------------------------------------------------------
#
# nn.Linear(4,3)
#
# Input Features  = 4
# Output Features = 3
#
# This means:
#
# Input
# [x1 x2 x3 x4]
#
#        │
#        ▼
#
# Linear Layer
#
#        │
#        ▼
#
# Output
# [Score_Class0, Score_Class1, Score_Class2]
#
# The model predicts scores (called logits)
# for 3 different classes.
#
model = nn.Linear(4, 3)


# ---------------------------------------------------------
# Define the Loss Function
# ---------------------------------------------------------
#
# CrossEntropyLoss is used for
# Multi-Class Classification.
#
# It combines:
#
# Softmax
# +
# Negative Log Likelihood Loss
#
# IMPORTANT:
#
# Do NOT apply Softmax manually before
# CrossEntropyLoss.
#
# CrossEntropyLoss does it internally.
#
criterion = nn.CrossEntropyLoss()


# ---------------------------------------------------------
# Create Random Input Data
# ---------------------------------------------------------
#
# torch.randn(5,4)
#
# Creates a tensor of random numbers
# from a normal distribution.
#
# Shape = (5,4)
#
# 5 = Number of samples
# 4 = Number of input features
#
# Example:
#
# [
#  [ 0.2  -1.1   0.5   0.9]
#  [ 0.7   0.3  -0.2   1.4]
#  ...
# ]
#
x = torch.randn(5, 4)


# ---------------------------------------------------------
# Create Target Labels
# ---------------------------------------------------------
#
# There are 5 training samples.
#
# Target class for each sample:
#
# Sample 1 → Class 0
# Sample 2 → Class 2
# Sample 3 → Class 1
# Sample 4 → Class 1
# Sample 5 → Class 0
#
# Notice:
#
# Target contains CLASS INDICES
# not one-hot vectors.
#
target = torch.tensor([0, 2, 1, 1, 0])


# ---------------------------------------------------------
# Forward Pass
# ---------------------------------------------------------
#
# Pass the input through the model.
#
# Output Shape:
#
# (5,3)
#
# Meaning:
#
# 5 samples
#
# Each sample has scores for
# 3 different classes.
#
prediction = model(x)


# ---------------------------------------------------------
# Calculate the Loss
# ---------------------------------------------------------
#
# Compare:
#
# Predicted Class Scores
#
#        VS
#
# Correct Class Labels
#
# CrossEntropyLoss automatically:
#
# Step 1:
# Applies Softmax
#
# Step 2:
# Computes the loss
#
loss = criterion(prediction, target)


# ---------------------------------------------------------
# Print the Loss
# ---------------------------------------------------------
#
# Example Output:
#
# tensor(1.2456, grad_fn=<NllLossBackward0>)
#
# Smaller loss means better predictions.
#
print(loss)