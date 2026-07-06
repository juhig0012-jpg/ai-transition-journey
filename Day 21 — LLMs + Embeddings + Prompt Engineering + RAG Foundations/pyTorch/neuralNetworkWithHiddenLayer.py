# Import PyTorch library
import torch

# Import the neural network module
import torch.nn as nn


# Create a neural network class by inheriting from nn.Module
class SimpleNN(nn.Module):

    # Constructor: runs automatically when an object of this class is created
    def __init__(self):

        # Initialize the parent class (nn.Module)
        # This enables PyTorch features like parameter tracking,
        # model saving/loading, GPU support, etc.
        super().__init__()

        # First Fully Connected (Linear) Layer
        # Input Features = 2
        # Output Features = 4
        #
        # Example:
        # Input:  [x1, x2]
        # Output: [h1, h2, h3, h4]
        self.fc1 = nn.Linear(2, 4)

        # Second Fully Connected Layer
        # Input Features = 4 (output from fc1)
        # Output Features = 1
        #
        # Example:
        # Input:  [h1, h2, h3, h4]
        # Output: [y]
        self.fc2 = nn.Linear(4, 1)

    # Defines how data moves through the neural network
    # This method is called automatically when we do:
    # output = model(input)
    def forward(self, x):

        # Pass input through the first linear layer
        #
        # Suppose input is:
        # [[2, 3]]
        #
        # Output becomes something like:
        # [[1.5, -0.7, 2.3, 0.9]]
        x = self.fc1(x)

        # Pass the output of fc1 into the second layer
        #
        # Input:
        # [[1.5, -0.7, 2.3, 0.9]]
        #
        # Output:
        # [[5.8]]
        x = self.fc2(x)

        # Return the final prediction
        return x