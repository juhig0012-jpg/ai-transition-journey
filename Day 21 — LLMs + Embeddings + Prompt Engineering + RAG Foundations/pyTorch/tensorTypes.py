import torch
#Scalar → 0D
a = torch.tensor(5)
#Vector → 1D
b = torch.tensor([1,2,3])
#Matrix → 2D
c = torch.tensor([[1,2],[3,4]])
#Tensor → 3D+
d = torch.tensor([
    [[1],[2]],
    [[3],[4]]
])
x = torch.tensor([[1,2,3],
                  [4,5,6]])

print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)
print(x.shape)
#Data Types
x = torch.tensor([1,2,3])

print(x.dtype)
#float type
x = torch.tensor([1,2,3],dtype=torch.float32)