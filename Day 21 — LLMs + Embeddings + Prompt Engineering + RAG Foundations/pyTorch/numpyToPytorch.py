import numpy as np

arr = np.array([1,2,3])
#NumPy → Tensor
tensor = torch.from_numpy(arr)

#Tensor → NumPy
tensor.numpy()