#Train a model to learn:

#y=3x+1
#Build an nn.Linear(1, 1) model.
#Use nn.MSELoss().
#Use the Adam optimizer.
#Train for 200 epochs.
#Print the loss every 20 epochs.
#Test the model with:
#x = [[10]]
#The prediction should be close to 31.
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
# y = 3x + 1
#
# Training Data
#
# x   y
# --------
# 1 → 4
# 2 → 7
# 3 → 10
# 4 → 13
# 5 → 16
#

X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y = torch.tensor([
    [4.0],
    [7.0],
    [10.0],
    [13.0],
    [16.0]
])


# ==========================================================
# Build the Model
# ==========================================================
#
# nn.Linear(1,1)
#
# Input Features = 1
# Output Features = 1
#
# The model learns:
#
# y = wx + b
#
# Initially:
#
# Weight (w) = Random
# Bias (b)   = Random
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
# The objective is to minimize this loss.
#

criterion = nn.MSELoss()


# ==========================================================
# Define Optimizer
# ==========================================================
#
# Adam Optimizer
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
# Train the model for 200 epochs.
#

epochs = 200

for epoch in range(epochs):

    # ------------------------------------------------------
    # Forward Pass
    # ------------------------------------------------------
    #
    # Compute predictions using:
    #
    # Prediction = Weight × X + Bias
    #
    prediction = model(X)

    # ------------------------------------------------------
    # Calculate Loss
    # ------------------------------------------------------
    #
    # Compare predictions with
    # the actual target values.
    #
    loss = criterion(prediction, y)

    # ------------------------------------------------------
    # Clear Previous Gradients
    # ------------------------------------------------------
    #
    # PyTorch accumulates gradients by default.
    # Remove old gradients before computing new ones.
    #
    optimizer.zero_grad()

    # ------------------------------------------------------
    # Backpropagation
    # ------------------------------------------------------
    #
    # Compute gradients of the loss
    # with respect to the model parameters.
    #
    loss.backward()

    # ------------------------------------------------------
    # Update Parameters
    # ------------------------------------------------------
    #
    # Adam updates:
    #
    # Weight
    # Bias
    #
    optimizer.step()

    # ------------------------------------------------------
    # Print Loss Every 20 Epochs
    # ------------------------------------------------------
    #
    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch+1:3d} | Loss = {loss.item():.6f}")


# ==========================================================
# Print Learned Parameters
# ==========================================================
#
# After training:
#
# Weight should be close to 3
# Bias should be close to 1
#

print("\nLearned Parameters")
print("------------------")
print("Weight:", model.weight.item())
print("Bias  :", model.bias.item())


# ==========================================================
# Test the Model
# ==========================================================
#
# Test Input:
#
# x = 10
#
# Expected Output:
#
# y = 3(10) + 1
# y = 31
#

test_input = torch.tensor([[10.0]])

# Disable gradient calculation during testing
with torch.no_grad():

    prediction = model(test_input)

print("\nTesting")
print("--------")
print("Input      :", test_input.item())
print("Prediction :", prediction.item())
print("Expected   :", 31.0)