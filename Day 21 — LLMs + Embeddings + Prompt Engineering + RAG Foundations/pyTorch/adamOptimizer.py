#As training progresses, the learned weight should become close to 2, and the bias should become close to 0 because the data follows the relationship:

#y=2x
# ==========================================================
# Import Required Libraries
# ==========================================================

# Import PyTorch
import torch

# Import Neural Network module
import torch.nn as nn


# ==========================================================
# Create Training Dataset
# ==========================================================
#
# We want the model to learn:
#
# y = 2x
#
# Training Samples:
#
# x   y
# -------
# 1 → 2
# 2 → 4
# 3 → 6
# 4 → 8
#

X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0]
])

y = torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0]
])


# ==========================================================
# Create the Model
# ==========================================================
#
# Linear Regression Model
#
# Input Features = 1
# Output Features = 1
#
# Mathematical Equation:
#
# y = wx + b
#
# Initially,
# weight (w) and bias (b)
# are random numbers.
#

model = nn.Linear(1, 1)


# ==========================================================
# Define Loss Function
# ==========================================================
#
# Mean Squared Error Loss
#
# Formula:
#
# Loss = Average((Prediction - Actual)^2)
#
# Smaller loss means
# better predictions.
#

criterion = nn.MSELoss()


# ==========================================================
# Define Optimizer
# ==========================================================
#
# Adam Optimizer
#
# Adam = Adaptive Moment Estimation
#
# It automatically adjusts
# the learning rate for each parameter.
#
# model.parameters()
# returns:
#
# Weight
# Bias
#
# lr = Learning Rate
#

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.1
)


# ==========================================================
# Training Loop
# ==========================================================
#
# Train the model for 100 epochs.
#

for epoch in range(100):

    # -------------------------------------
    # Forward Pass
    # -------------------------------------
    #
    # Pass input through the model.
    #
    # Formula:
    #
    # Prediction = Weight × Input + Bias
    #
    prediction = model(X)

    # -------------------------------------
    # Calculate Loss
    # -------------------------------------
    #
    # Compare:
    #
    # Prediction
    #        VS
    # Actual Output
    #
    loss = criterion(prediction, y)

    # -------------------------------------
    # Clear Previous Gradients
    # -------------------------------------
    #
    # PyTorch stores gradients.
    #
    # Remove old gradients before
    # computing new ones.
    #
    optimizer.zero_grad()

    # -------------------------------------
    # Backpropagation
    # -------------------------------------
    #
    # Compute gradients
    # of every trainable parameter.
    #
    loss.backward()

    # -------------------------------------
    # Update Parameters
    # -------------------------------------
    #
    # Adam updates:
    #
    # Weight
    # Bias
    #
    # so that loss becomes smaller.
    #
    optimizer.step()


# ==========================================================
# Print Final Parameters
# ==========================================================
#
# After training,
# Weight should be close to 2
#
# Bias should be close to 0
#

print("Weight:", model.weight)

print("Bias:", model.bias)