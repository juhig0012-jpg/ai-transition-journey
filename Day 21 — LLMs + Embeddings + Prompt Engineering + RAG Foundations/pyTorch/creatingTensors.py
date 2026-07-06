import torch
#Zeros
x=torch.zeros(3,4)
print(x)

#ones
y=torch.ones(2,3)
print(y)

#Random
z=torch.rand(3,3)
print(z)

#integer random
a=torch.randint(0,10,(3,3))
print(a)

#Identity Matrix
b=torch.eye(4)
print(b)
