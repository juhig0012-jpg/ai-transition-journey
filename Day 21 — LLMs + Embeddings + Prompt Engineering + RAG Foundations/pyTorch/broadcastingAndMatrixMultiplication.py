#Broadcasting allows for automatic expansion of dimensions to facilitate arithmetic operations on tensors of different shapes.
#Matrix multiplication enables efficient computations essential for neural network operations.
import torch

tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])

tensor_b = torch.tensor([[10, 20, 30]]) 

broadcasted_result = tensor_a + tensor_b 
print(f"Broadcasted Addition Result: \n{broadcasted_result}")

matrix_multiplication_result = torch.matmul(tensor_a, tensor_a.T)
print(f"Matrix Multiplication Result (tensor_a * tensor_a^T): \n{matrix_multiplication_result}")