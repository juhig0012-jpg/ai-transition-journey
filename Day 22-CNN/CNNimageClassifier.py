# ==========================================================
# Mini Project: Build a CNN Image Classifier
#
# Input Image Size  : 32 x 32
# Color Channels    : 3 (RGB)
# Number of Classes : 10
#
# CNN Architecture:
#
# Conv2d(3,16,3,padding=1)
# ReLU
# MaxPool2d(2)
#
# Conv2d(16,32,3,padding=1)
# ReLU
# MaxPool2d(2)
#
# Flatten
# Linear(32*8*8,10)
# ==========================================================

# Import PyTorch
import torch

# Import Neural Network module
import torch.nn as nn


# ==========================================================
# Step 1: Define CNN Model
# ==========================================================

# Every custom neural network should inherit from nn.Module
class ImageClassifier(nn.Module):

    # Constructor
    def __init__(self):

        # Call parent constructor
        super().__init__()

        # --------------------------------------------------
        # First Convolution Layer
        #
        # Input Channels  = 3 (RGB)
        # Output Channels = 16
        # Kernel Size     = 3x3
        # Padding = 1 keeps height and width unchanged
        #
        # Input :
        # (Batch,3,32,32)
        #
        # Output:
        # (Batch,16,32,32)
        # --------------------------------------------------
        self.conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=16,
            kernel_size=3,
            padding=1
        )

        # ReLU Activation
        self.relu1 = nn.ReLU()

        # Max Pooling
        #
        # Kernel = 2x2
        #
        # Reduces:
        #
        # 32x32 → 16x16
        #
        self.pool1 = nn.MaxPool2d(kernel_size=2)

        # --------------------------------------------------
        # Second Convolution Layer
        #
        # Input :
        # (Batch,16,16,16)
        #
        # Output:
        # (Batch,32,16,16)
        # --------------------------------------------------
        self.conv2 = nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=3,
            padding=1
        )

        # ReLU Activation
        self.relu2 = nn.ReLU()

        # Second Max Pool
        #
        # 16x16 → 8x8
        #
        self.pool2 = nn.MaxPool2d(kernel_size=2)

        # Flatten Layer
        #
        # Converts:
        #
        # (Batch,32,8,8)
        #
        # into
        #
        # (Batch,2048)
        #
        self.flatten = nn.Flatten()

        # Fully Connected Layer
        #
        # Input Features:
        #
        # 32 × 8 × 8 = 2048
        #
        # Output:
        #
        # 10 class scores
        #
        self.fc = nn.Linear(
            32 * 8 * 8,
            10
        )

    # ======================================================
    # Forward Pass
    # ======================================================
    def forward(self, x):

        print("Input Shape :", x.shape)

        # ---------------------------
        # First Convolution
        # ---------------------------
        x = self.conv1(x)
        print("After Conv1 :", x.shape)

        # ReLU
        x = self.relu1(x)
        print("After ReLU1 :", x.shape)

        # Max Pool
        x = self.pool1(x)
        print("After Pool1 :", x.shape)

        # ---------------------------
        # Second Convolution
        # ---------------------------
        x = self.conv2(x)
        print("After Conv2 :", x.shape)

        # ReLU
        x = self.relu2(x)
        print("After ReLU2 :", x.shape)

        # Max Pool
        x = self.pool2(x)
        print("After Pool2 :", x.shape)

        # ---------------------------
        # Flatten
        # ---------------------------
        x = self.flatten(x)
        print("After Flatten :", x.shape)

        # ---------------------------
        # Fully Connected Layer
        # ---------------------------
        x = self.fc(x)
        print("Final Output :", x.shape)

        return x


# ==========================================================
# Step 2: Create Model
# ==========================================================

model = ImageClassifier()

print(model)


# ==========================================================
# Step 3: Generate Random Images
# ==========================================================

# Batch Size = 4
#
# Channels = 3
#
# Height = 32
#
# Width = 32
#
x = torch.randn(4, 3, 32, 32)


# ==========================================================
# Step 4: Forward Pass
# ==========================================================

output = model(x)


# ==========================================================
# Step 5: Verify Output Shape
# ==========================================================

print("\nExpected Output Shape : torch.Size([4,10])")
print("Actual Output Shape   :", output.shape)