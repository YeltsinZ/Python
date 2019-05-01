from numpy import *

arr = array([
    [1,2,3,4,5,6],
    [3,4,5,6,7,6]
])

print(arr)
print(arr.dtype) #return the type of the 2D array
print(arr.ndim) # retuns the no.of dimensions in the array
print(arr.shape) #return the no.of rows and columns of the array
print(arr.size) #returns the entire size of the whole array

#coverting 2D into 1D
arr2 = arr.flatten()
print(arr2)

#converting 1D into 3D
arr3 = arr2.reshape(2,2,3)
print(arr3)

