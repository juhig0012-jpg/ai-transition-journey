import numpy as np
#0 d array
zeroDarray = np.array(42)
#1 d array
oneDarray = np.array([1,2,3,4])
#two d array
twoDarray = np.array([[1,2,3],[4,5,6]])
#three d array
threeDarray = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
#check dimensions
print(oneDarray.ndim)
print(twoDarray.ndim)
print(threeDarray.ndim)

#creating higher dimensional array
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)