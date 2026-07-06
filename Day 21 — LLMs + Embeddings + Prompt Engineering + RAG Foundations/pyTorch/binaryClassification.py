# ==========================================================
# Import Required Libraries
# ==========================================================

import torch
import torch.nn as nn

# ==========================================================
# Create Training Data
# ==========================================================
#
# We have 6 samples.
# Each sample has 2 input features.
#
# Input Features:
#
# [1,1] → Class 0
# [2,1] → Class 0
# [2,2] → Class 0
# [4,4] → Class 1
# [5,5] → Class 1
# [6,5] → Class 1
#

X = torch.tensor([
    [1.0, 1.0],
    [2.0, 1.0],
    [2.0, 2.0],
    [4.0, 4.0],
    [5.0, 5.0],
    [6.0, 5.0]
])

# Target Labels
#
# Shape = (6,1)
#
# Binary Classification:
# 0 = Negative Class
# 1 = Positive Class
#

y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0],
    [1.0],
    [1.0]
])

# ==========================================================
# Build Neural Network
# ==========================================================
#
# Architecture
#
# Input (2)
#      │
#      ▼
# Linear(2 → 4)
#      │
#      ▼
# ReLU
#      │
#      ▼
# Linear(4 → 1)
#      │
#      ▼
# Output (LOGITS)
#
# IMPORTANT:
# Do NOT use Sigmoid here because
# BCEWithLogitsLoss applies Sigmoid internally.
#

model = nn.Sequential(

    # Hidden Layer
    nn.Linear(2, 4),

    # Activation Function
    nn.ReLU(),

    # Output Layer
    #
    # Produces ONE LOGIT
    nn.Linear(4, 1)
)

# ==========================================================
# Loss Function
# ==========================================================
#
# BCEWithLogitsLoss =
#
# Sigmoid
#        +
# Binary Cross Entropy
#
# It is more numerically stable than
# nn.Sigmoid() + nn.BCELoss()
#

criterion = nn.BCEWithLogitsLoss()

# ==========================================================
# Optimizer
# ==========================================================

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# ==========================================================
# Training
# ==========================================================

epochs = 1000

for epoch in range(epochs):

    # ----------------------------
    # Forward Pass
    # ----------------------------
    #
    # Output is LOGITS
    # (not probabilities)
    #
    logits = model(X)

    # ----------------------------
    # Calculate Loss
    # ----------------------------
    #
    # BCEWithLogitsLoss internally:
    #
    # Logits
    #    ↓
    # Sigmoid
    #    ↓
    # Binary Cross Entropy
    #
    loss = criterion(logits, y)

    # ----------------------------
    # Clear Previous Gradients
    # ----------------------------
    optimizer.zero_grad()

    # ----------------------------
    # Compute Gradients
    # ----------------------------
    loss.backward()

    # ----------------------------
    # Update Parameters
    # ----------------------------
    optimizer.step()

    # Print Loss Every 100 Epochs
    if (epoch + 1) % 100 == 0:
        print(f"Epoch {epoch+1} Loss = {loss.item():.4f}")

# ==========================================================
# Testing
# ==========================================================

print("\nRaw Logits")

with torch.no_grad():

    logits = model(X)

    print(logits)

# ==========================================================
# Convert Logits to Probabilities
# ==========================================================
#
# During inference,
# apply Sigmoid manually.
#
# Probability =
#
# 0 → Class 0
#
# 1 → Class 1
#

probabilities = torch.sigmoid(logits)

print("\nProbabilities")
print(probabilities)

# ==========================================================
# Convert Probability into Class
# ==========================================================
#
# Threshold = 0.5
#
# >= 0.5 → Class 1
#
# < 0.5 → Class 0
#

predicted_classes = (probabilities >= 0.5).float()

print("\nPredicted Classes")
print(predicted_classes)

print("\nActual Classes")
print(y)