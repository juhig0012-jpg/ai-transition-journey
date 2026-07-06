# ==========================================================
# Mini Project
# Learn the equation:
#
#           y = 5x + 2
#
# Save the trained model
# Load the saved model
# Predict for x = 10
# ==========================================================

# Import PyTorch
import torch

# Import Neural Network module
import torch.nn as nn


# ==========================================================
# Step 1: Create Dataset
# ==========================================================

# Input values (x)
X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

# Target values using:
# y = 5x + 2
#
# x=1 → y=7
# x=2 → y=12
# x=3 → y=17
# x=4 → y=22
# x=5 → y=27
y = torch.tensor([
    [7.0],
    [12.0],
    [17.0],
    [22.0],
    [27.0]
])


# ==========================================================
# Step 2: Build Model
# ==========================================================

# Create a Linear Regression model
#
# Input Features = 1
# Output Features = 1
#
# Model equation:
#
# prediction = weight × x + bias
#
model = nn.Linear(1, 1)


# ==========================================================
# Step 3: Define Loss Function
# ==========================================================

# Mean Squared Error
criterion = nn.MSELoss()


# ==========================================================
# Step 4: Define Optimizer
# ==========================================================

# Stochastic Gradient Descent
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)


# ==========================================================
# Step 5: Train the Model
# ==========================================================

epochs = 300

for epoch in range(epochs):

    # Forward Pass
    predictions = model(X)

    # Calculate loss
    loss = criterion(predictions, y)

    # Remove old gradients
    optimizer.zero_grad()

    # Calculate new gradients
    loss.backward()

    # Update weight and bias
    optimizer.step()

    # Print loss every 30 epochs
    if (epoch + 1) % 30 == 0:
        print(f"Epoch {epoch+1:3d} | Loss = {loss.item():.6f}")


# ==========================================================
# Step 6: Save Model
# ==========================================================

# Save only the learned parameters
#
# This creates:
#
# linear_model.pth
#
torch.save(model.state_dict(), "linear_model.pth")

print("\nModel saved successfully!")


# ==========================================================
# Step 7: Create a New Model
# ==========================================================

# Create a completely new model
#
# Currently it has random weights
#
loaded_model = nn.Linear(1, 1)


# ==========================================================
# Step 8: Load Saved Weights
# ==========================================================

# Load learned weights into new model
loaded_model.load_state_dict(
    torch.load("linear_model.pth")
)

print("Model loaded successfully!")


# ==========================================================
# Step 9: Set Evaluation Mode
# ==========================================================

# Disable training-specific behavior
#
# (Important for models containing
# Dropout or BatchNorm layers)
#
loaded_model.eval()


# ==========================================================
# Step 10: Predict
# ==========================================================

# Disable gradient calculation
with torch.no_grad():

    # Test input
    test = torch.tensor([[10.0]])

    # Predict output
    prediction = loaded_model(test)

    print("\nPrediction")

    print("Input :", test.item())

    print("Output:", prediction.item())