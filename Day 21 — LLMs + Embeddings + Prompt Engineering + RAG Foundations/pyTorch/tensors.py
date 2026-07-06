import torch

tensor_1d = torch.tensor([1, 2, 3])
print("1D Tensor (Vector):")
print(tensor_1d)
print()

tensor_2d = torch.tensor([[1, 2], [3, 4]])
print("2D Tensor (Matrix):")
print(tensor_2d)
print()

random_tensor = torch.rand(2, 3)
print("Random Tensor (2x3):")
print(random_tensor)
print()

zeros_tensor = torch.zeros(2, 3)
print("Zeros Tensor (2x3):")
print(zeros_tensor)
print()

ones_tensor = torch.ones(2, 3)
print("Ones Tensor (2x3):")
print(ones_tensor)