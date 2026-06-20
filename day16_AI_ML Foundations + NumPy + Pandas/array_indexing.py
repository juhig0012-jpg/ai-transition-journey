import numpy as np
#import first element from array
arr = np.array([1, 2, 3, 4])
print(arr[0])
#Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])
#access 2d array
#Access the element on the first row, second column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
#Access 3d array
#Access the third element of the second array of the first array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
#negative indexing
#Print the last element from the 2nd dim:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])