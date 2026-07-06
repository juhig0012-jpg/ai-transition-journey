import torch

tensor = torch.tensor([[1, 2], [3, 4], [5, 6]])

element = tensor[1, 0]
print(f"Indexed Element (Row 1, Column 0): {element}")  
slice_tensor = tensor[:2, :]
print(f"Sliced Tensor (First two rows): \n{slice_tensor}")

reshaped_tensor = tensor.view(2, 3)
print(f"Reshaped Tensor (2x3): \n{reshaped_tensor}")

#Addition
a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])

print(a+b)

#subtraction
print(a-b)

#Multiplication
print(a*b)

#Division
print(a/b)

#power
print(a**2)

#Matrix Multiplication
A = torch.tensor([[1,2],
                  [3,4]])

B = torch.tensor([[5,6],
                  [7,8]])

print(torch.matmul(A,B))

#Tensor Indexing
x = torch.tensor([[1,2,3],
                  [4,5,6]])
#First row
x[0]
#Second row
x[1]

#First element
x[0][0]

#Reshape
x = torch.arange(12)

print(x)
x = x.reshape(3,4)

#Flatten
x.flatten()

#Transpose
y=x.T
print(y)

#Mean
x.mean()

#Sum
z=x.sum()

#Maximum
print(x.max())

#Minimum
print(x.min())