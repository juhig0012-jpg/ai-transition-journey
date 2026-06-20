#Without ufunc, we can use Python's built-in zip() method:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

#With ufunc, we can use the add() function:
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

#Create your own ufunc for addition:
#The frompyfunc() method takes the following arguments:

#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

#Check if a Function is a ufunc

print(type(np.add))

#Use an if statement to check if the function is a ufunc or not:

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

#Addition
#Add the values in arr1 to the values in arr2:
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

#subtraction 
#Subtract the values in arr2 from the values in arr1:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)

#multiplication
#Multiply the values in arr1 with the values in arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)

#division
#Divide the values in arr1 with the values in arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)

#power
#Raise the valules in arr1 to the power of values in arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)

#Return the remainders:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)

#Return the quotient and mod:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)

#Return the absolute values of the array:
arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)

#Rounding Decimals
#There are primarily five ways of rounding off decimals in NumPy:

#truncation
#fix
#rounding
#floor
#ceil

#Truncate elements of following array:
arr = np.trunc([-3.1666, 3.6667])

print(arr)

#Same example, using fix():
arr = np.fix([-3.1666, 3.6667])

print(arr)

#Round off 3.1666 to 2 decimal places:
arr = np.around(3.1666, 2)

print(arr)

#Floor the elements of following array:
arr = np.floor([-3.1666, 3.6667])

print(arr)

#Ceil the elements of following array:
arr = np.ceil([-3.1666, 3.6667])

print(arr)

#Find log at base 2 of all elements of following array:
arr = np.arange(1, 10)

print(np.log2(arr))

#Find log at base 10 of all elements of following array:
arr = np.arange(1, 10)

print(np.log10(arr))

#Find log at base e of all elements of following array:

arr = np.arange(1, 10)

print(np.log(arr))

#Log at Any Base
#NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:
from math import log
nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

#Summations
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)

#Perform summation in the following array over 1st axis:

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)

#Cummulative Sum
#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)

#Find the product of the elements of this array:
arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)

#Find the product of the elements of two arrays:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)

#Perform product in the following array over 1st axis:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

#Cummulative Product
arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)

#differences
#E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

#discrete difference
#Compute discrete difference of the following array twice:
arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)
#Returns: [5 -30] because: 15-10=5, 25-15=10, and 5-25=-20 AND 10-5=5 and -20-10=-30

#Find the LCM of the following two numbers:
num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

#Finding LCM in Arrays
#Find the LCM of the values of the following array:
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

#Find the LCM of all values of an array where the array contains all integers from 1 to 10:
arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)

#Find the HCF of the following two numbers:
num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)

#Find the GCD for all of the numbers in the following array:
arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)

#trignometric functions
#Find sine value of PI/2:
x = np.sin(np.pi/2)

print(x)

#Find sine values for all of the values in arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

#Convert Degrees Into Radians
#By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.

#Note: radians values are pi/180 * degree_values.

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

#Convert all of the values in following array arr to degrees:
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)

#Find the angle of 1.0:

x = np.arcsin(1.0)

print(x)

#Find the angle for all of the sine values in the array
arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

#Find the hypotenues for 4 base and 3 perpendicular:
base = 3
perp = 4

x = np.hypot(base, perp)

print(x)

#NumPy Hyperbolic Functions
#Find sinh value of PI/2:

x = np.sinh(np.pi/2)

print(x)

#Find cosh values for all of the values in arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)

#Find the angle of 1.0:
x = np.arcsinh(1.0)

print(x)

#Find the angle for all of the tanh values in array:
arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)

#sets

#Convert following array with repeated elements to a set:
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)

#Find union of the following two set arrays:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)

#Find intersection of the following two set arrays:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)

#Find the difference of the set1 from set2:

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)

#Find the symmetric difference of the set1 and set2:
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)

