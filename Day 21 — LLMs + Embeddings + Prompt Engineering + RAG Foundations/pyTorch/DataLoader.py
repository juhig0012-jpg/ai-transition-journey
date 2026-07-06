# Import the main PyTorch library
import torch

# Import the Dataset class
# Dataset is the base class used to create custom datasets
from torch.utils.data import Dataset

# Import the DataLoader class
# DataLoader loads data in batches and can shuffle the data
from torch.utils.data import DataLoader


# Create a custom dataset by inheriting from Dataset
class StudentDataset(Dataset):

    # Constructor
    # This runs automatically when the dataset object is created
    def __init__(self):

        # Input features (X)
        # Shape = (4, 1)
        # Four samples:
        # Student 1 -> 1
        # Student 2 -> 2
        # Student 3 -> 3
        # Student 4 -> 4
        self.X = torch.tensor([
            [1.0],
            [2.0],
            [3.0],
            [4.0]
        ])

        # Target values (y)
        # Shape = (4, 1)
        # Corresponding outputs
        self.y = torch.tensor([
            [20.0],
            [40.0],
            [60.0],
            [80.0]
        ])

    # Returns the total number of samples
    # DataLoader calls this automatically
    def __len__(self):

        # There are 4 samples
        return len(self.X)

    # Returns one sample at a time
    # DataLoader calls this automatically using an index
    def __getitem__(self, index):

        # Return one input and its corresponding label
        return self.X[index], self.y[index]


# Create an object of the custom dataset
dataset = StudentDataset()


# Create a DataLoader
loader = DataLoader(

    # Dataset to load
    dataset,

    # Number of samples per batch
    # Each batch will contain 2 samples
    batch_size=2,

    # Shuffle the dataset before every epoch
    # Helps the model learn better during training
    shuffle=True
)


# Iterate through every batch in the DataLoader
for X_batch, y_batch in loader:

    # Print the input batch
    print(X_batch)

    # Print the corresponding output batch
    print(y_batch)