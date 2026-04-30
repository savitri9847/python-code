import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# newarr = np.add(arr1,arr2)
# print("Addition is",newarr )
# # summation

# arr3 =  np.array([1,2,3])
# arr4 = np.array([4,5,6])
# newarr1 = np.sum([arr3,arr4])
# print("summation is ", newarr1)

# cumulative summation
# arr = np.array([1,2,3,4,5,6])
# newarr2 = np.cumsum(arr)
# print("cumulative is ", newarr2)

# numpy product
arr = np.array([1,2,3,4,5,6,7,8,])
x =np.prod(arr)
print("the product is:",x)

# product of two array using the prod() universal function 
# arr1 =np.array([1,2,3])
# arr2 =np.array([4,5,6])
# x = np.prod([arr1,arr2], axis=0)
# print("The product is:", x)
# ========row===========
# arr1 =np.array([1,2,3])
# arr2 =np.array([4,5,6])
# x = np.prod([arr1,arr2], axis=1)
# print("The product is:", x)

# cumulative product or array
arr3 = np.array([1,2,3,4,5,6])
x = np.cumprod(arr3)
# print("The cumulative product is:",x)

arr = np.array([10,15,25,5])
newarr =np.diff(arr)
# print(newarr)
arr = np.array([10,15,25,5])
newarr =np.diff(arr,n=2)
print(newarr)

