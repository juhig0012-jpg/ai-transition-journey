#Step 1: Define the Neural Network Class
#In this step, we’ll define a class that inherits from torch.nn.Module. We’ll create a simple neural network with an input layer, a hidden layer and an output layer.
# ==========================================================
# Import Required Libraries
# ==========================================================

# Import the main PyTorch library.
# It provides tensors, mathematical operations,
# automatic differentiation (Autograd), and many utilities.
import torch

# Import the neural network (nn) module from PyTorch.
# The nn module contains pre-built layers such as:
# - Linear (Fully Connected Layer)
# - Conv2d (Convolution Layer)
# - LSTM
# - GRU
# - Dropout
# - BatchNorm
# - Loss Functions
import torch.nn as nn


# ==========================================================
# Define a Neural Network Class
# ==========================================================

# Create a new neural network class named SimpleNN.
#
# Every custom neural network in PyTorch must inherit
# from nn.Module.
#
# nn.Module provides:
# - Parameter management
# - Model saving/loading
# - GPU support
# - Forward propagation support
class SimpleNN(nn.Module):

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------

    # __init__() is automatically called when an object
    # of this class is created.
    #
    # It is used to initialize all layers of the network.
    def __init__(self):

        # Call the constructor of the parent class (nn.Module).
        #
        # This is mandatory.
        #
        # It initializes internal PyTorch components that
        # keep track of all trainable parameters.
        super(SimpleNN, self).__init__()

        # --------------------------------------------------
        # First Fully Connected Layer
        # --------------------------------------------------

        # Create a Linear (Dense/Fully Connected) layer.
        #
        # Syntax:
        # nn.Linear(input_features, output_features)
        #
        # Here:
        # Input neurons  = 2
        # Output neurons = 4
        #
        # PyTorch automatically creates:
        # Weight matrix
        # Bias vector
        #
        # This layer learns:
        # Output = Input × Weight + Bias
        self.fc1 = nn.Linear(2, 4)

        # --------------------------------------------------
        # Second Fully Connected Layer
        # --------------------------------------------------

        # This layer receives 4 outputs from fc1.
        #
        # It produces only one output.
        #
        # So:
        # Input neurons = 4
        # Output neurons = 1
        self.fc2 = nn.Linear(4, 1)


    # ======================================================
    # Forward Propagation
    # ======================================================

    # The forward() method defines how data flows
    # through the neural network.
    #
    # PyTorch automatically calls forward()
    # whenever you write:
    #
    # output = model(input)
    #
    # You NEVER call forward() directly.
    def forward(self, x):

        # Pass input through the first linear layer.
        #
        # fc1(x) performs:
        #
        # Output = x × Weight + Bias
        #
        # The output shape becomes:
        # (batch_size, 4)
        #
        # torch.relu() applies the ReLU activation function.
        #
        # ReLU Formula:
        #
        # ReLU(x) = max(0, x)
        #
        # It converts all negative values to zero.
        #
        # Example:
        # [-5, 2, -1, 8]
        #
        # becomes
        #
        # [0, 2, 0, 8]
        x = torch.relu(self.fc1(x))

        # Pass the output of fc1 into fc2.
        #
        # This computes the final prediction.
        #
        # No activation function is used here.
        #
        # Final output shape:
        # (batch_size, 1)
        x = self.fc2(x)

        # Return the final output.
        return x