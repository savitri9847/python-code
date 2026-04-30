# copy vs view
import numpy as np 
# arr = np.array([1,2,3,4,5])
# x = np.array.copy()
# arr[0] = 42
# # this is the copyp
# print(arr)
# print(x)
# arr2 = np.array([1,2,3,4,5])
# # y is the view of art2, it share the same data 
# y = arr2.view()

# arr2[0] = 42
# print(arr2)
# print(y)

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# newwarr = arr.reshape(10,2)
# print(newwarr)

# print(newwarr.indim)

# flattering milti dimenstion array to array 
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
newwarr = arr.reshape(-1)
print(newwarr)
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

print(arr)