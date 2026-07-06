# Import the functional module from torch.nn
# It contains activation functions like ReLU, Sigmoid, Softmax, etc.
import torch.nn as nn

import torch.nn.functional as F

# Create a neural network class by inheriting from nn.Module
class SimpleNN(nn.Module):

    # Constructor: runs automatically when the model object is created
    def __init__(self):

        # Initialize the parent class (nn.Module)
        # This enables PyTorch features such as:
        # - Automatic parameter tracking
        # - Saving and loading the model
        # - Moving the model to GPU
        super().__init__()

        # First Fully Connected (Linear) Layer
        #
        # Input Features = 2
        # Output Features = 4
        #
        # Example:
        # Input : [x1, x2]
        # Output: [h1, h2, h3, h4]
        self.fc1 = nn.Linear(2, 4)

        # Second Fully Connected (Linear) Layer
        #
        # Input Features = 4
        # Output Features = 1
        #
        # Example:
        # Input : [h1, h2, h3, h4]
        # Output: [y]
        self.fc2 = nn.Linear(4, 1)

    # Defines how the input data flows through the network
    # This method is automatically called when we write:
    # output = model(input)
    def forward(self, x):

        # Step 1: Pass the input through the first linear layer
        #
        # Example:
        # Input:
        # [[2, 3]]
        #
        # After fc1:
        # [[-1.5, 2.4, 0.8, -0.3]]
        #
        # Step 2: Apply the ReLU activation function
        #
        # ReLU(x) = max(0, x)
        #
        # Negative values become 0.
        #
        # Before ReLU:
        # [-1.5, 2.4, 0.8, -0.3]
        #
        # After ReLU:
        # [0.0, 2.4, 0.8, 0.0]
        #
        # ReLU introduces non-linearity, allowing the network
        # to learn complex patterns.
        x = F.relu(self.fc1(x))

        # Step 3: Pass the activated output through
        # the second linear layer
        #
        # Input:
        # [0.0, 2.4, 0.8, 0.0]
        #
        # Output:
        # [5.6]
        x = self.fc2(x)

        # Return the final prediction
        return x