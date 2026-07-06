#PyTorch facilitates GPU acceleration, enabling much faster computations which is especially important in deep learning due to the extensive matrix operations involved. By transferring tensors to the GPU, you can significantly reduce training times and improve performance.
import torch

# Select device (GPU if available, otherwise CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Create tensors
tensor_size = (10000, 10000)

a = torch.randn(tensor_size).to(device)
b = torch.randn(tensor_size).to(device)

# Tensor addition
c = a + b

# Move result to CPU for printing
# ==========================================================
# PyTorch GPU/CPU Acceleration Example
# ==========================================================
# PyTorch can perform computations on either:
# 1. CPU (Central Processing Unit)
# 2. GPU (Graphics Processing Unit)
#
# GPUs are much faster than CPUs for deep learning because they
# can perform thousands of mathematical operations simultaneously.
#
# This program automatically checks whether an NVIDIA GPU is
# available. If yes, it uses the GPU; otherwise, it uses the CPU.
# ==========================================================

# Import the PyTorch library
import torch

# ----------------------------------------------------------
# Select the computing device
# ----------------------------------------------------------

# torch.cuda.is_available()
# Returns True if an NVIDIA CUDA-enabled GPU is available.
#
# If True  -> device = "cuda"
# If False -> device = "cpu"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Display the device being used
print(f"Using device: {device}")

# ----------------------------------------------------------
# Create large tensors
# ----------------------------------------------------------

# Define the size of the tensors.
# This creates a matrix with:
# 10,000 rows
# 10,000 columns
tensor_size = (10000, 10000)

# Create a tensor filled with random numbers.
# torch.randn() generates numbers from a standard normal
# distribution (mean = 0, standard deviation = 1).
#
# .to(device) moves the tensor to the selected device
# (CPU or GPU).
a = torch.randn(tensor_size).to(device)

# Create another random tensor of the same size
b = torch.randn(tensor_size).to(device)

# ----------------------------------------------------------
# Perform Tensor Addition
# ----------------------------------------------------------

# Add the two tensors element-by-element.
#
# If using GPU:
# Addition is performed on the GPU.
#
# If using CPU:
# Addition is performed on the CPU.
c = a + b

# ----------------------------------------------------------
# Print the Result
# ----------------------------------------------------------

# If the tensor is stored on the GPU,
# move it back to the CPU before printing.
#
# .cpu() copies the tensor from GPU memory
# to CPU memory.
#
# .shape returns the dimensions of the tensor.
print("Result shape:", c.cpu().shape)

# ----------------------------------------------------------
# Check whether the program is running on GPU
# ----------------------------------------------------------

# device.type returns:
# "cuda" -> NVIDIA GPU
# "cpu"  -> CPU
if device.type == "cuda":

    # Create another pair of tensors directly on the GPU
    tensor_size = (10000, 10000)

    # Random tensor stored directly in GPU memory
    a = torch.randn(tensor_size, device=device)

    # Another random tensor stored in GPU memory
    b = torch.randn(tensor_size, device=device)

    # GPU performs tensor addition
    c = a + b

    # Move result to CPU for displaying its shape
    print("Result shape (moved to CPU for printing):", c.cpu().shape)

    # ------------------------------------------------------
    # Display GPU Memory Usage
    # ------------------------------------------------------

    print("Current GPU memory usage:")

    # torch.cuda.memory_allocated()
    # Returns the amount of GPU memory currently occupied
    # by tensors.
    #
    # Divide by (1024 ** 2) to convert bytes into MB.
    print(f"Allocated: {torch.cuda.memory_allocated(device) / (1024 ** 2):.2f} MB")

    # torch.cuda.memory_reserved()
    # Returns the total GPU memory reserved by PyTorch.
    #
    # Reserved memory is larger than allocated memory because
    # PyTorch keeps extra memory for faster future allocations.
    print(f"Cached (Reserved): {torch.cuda.memory_reserved(device) / (1024 ** 2):.2f} MB")

# ----------------------------------------------------------
# If GPU is not available
# ----------------------------------------------------------
else:

    # Inform the user that computations are running on CPU.
    print("\nRunning on CPU.")

    # GPU memory statistics cannot be displayed
    # because CUDA is unavailable.
    print("GPU memory information is not available.")