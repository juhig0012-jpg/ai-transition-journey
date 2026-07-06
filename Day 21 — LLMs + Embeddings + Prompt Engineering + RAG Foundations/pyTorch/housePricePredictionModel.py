# Import the PyTorch library
import torch

# Import the neural network module
import torch.nn as nn


# ============================
# Create Training Data
# ============================

# Input values (features)
# Shape: (4,1)
# X = [[1],
#      [2],
#      [3],
#      [4]]
X = torch.tensor([[1], [2], [3], [4]], dtype=torch.float32)

# Target values (labels)
# The expected relationship is y = 2x
# Shape: (4,1)
# y = [[2],
#      [4],
#      [6],
#      [8]]
y = torch.tensor([[2], [4], [6], [8]], dtype=torch.float32)


# ============================
# Create the Model
# ============================

# Create one Linear layer
#
# nn.Linear(in_features, out_features)
#
# Here:
# input features = 1
# output features = 1
#
# Mathematical equation:
#
# y = Wx + b
#
# where
# W = weight
# b = bias
#
# Initially W and b are random.
# During training they will be updated.
model = nn.Linear(1, 1)


# ============================
# Loss Function
# ============================

# Mean Squared Error (MSE)
#
# Formula:
#
# loss = average((actual - predicted)^2)
#
# Smaller loss means better predictions.
criterion = nn.MSELoss()


# ============================
# Optimizer
# ============================

# Stochastic Gradient Descent (SGD)
#
# model.parameters()
# returns all trainable parameters
# (weight and bias)
#
# lr = learning rate
# Determines how much weights change each step.
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)


# ============================
# Training Loop
# ============================

# Train for 500 iterations (epochs)
for epoch in range(500):

    # -------------------------
    # Forward Pass
    # -------------------------

    # Pass input through the model
    #
    # Predicted values:
    # initially something random
    #
    # Example:
    # [[1.1],
    #  [2.2],
    #  [3.3],
    #  [4.4]]
    pred = model(X)


    # -------------------------
    # Calculate Loss
    # -------------------------

    # Compare predicted values with
    # actual values.
    #
    # Lower loss = better model.
    loss = criterion(pred, y)


    # -------------------------
    # Clear Previous Gradients
    # -------------------------

    # Gradients accumulate in PyTorch.
    # So before calculating new gradients,
    # clear the old ones.
    optimizer.zero_grad()


    # -------------------------
    # Backpropagation
    # -------------------------

    # Compute gradients of loss
    # with respect to every parameter.
    #
    # Calculates:
    #
    # dLoss/dWeight
    # dLoss/dBias
    loss.backward()


    # -------------------------
    # Update Parameters
    # -------------------------

    # Update weight and bias
    # using the gradients.
    optimizer.step()


# ============================
# Testing
# ============================

# Give a new input value = 5
#
# Expected output:
# 10
#
# Since the model learned:
#
# y = 2x
#
# It should predict something close to:
#
# tensor([[10.]])
print(model(torch.tensor([[5.0]])))

#What happens internally?
#Step 1: Model is created

#Initially the model has random parameters.

#Suppose:

#Weight = 0.37
#Bias   = 1.52

#So the model equation is

#y = 0.37x + 1.52

#This is obviously incorrect.

#Step 2: First Forward Pass

#Input

#1
#2
#y = 2x

#Repeat 500 Times
#y = 2x
#What does the model learn?

#Initially:

#Weight = Random
#Bias = Random

#After training:

#Weight ≈ 2

#Bias ≈ 0

#So the model has learned:

#y = 2x