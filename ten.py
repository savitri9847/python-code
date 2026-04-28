import numpy as np
# without function 
# x = [1,2,3,4]
# y=  [5,6,7,8]
# z = []
# for i, j in zip(x,y):
#     z.append(i+j)
    
# print(z)
# # with unfunc
# x = [1,2,3,4]
# y = [4,5,6,7]
# z = np.add(x,y)
# print(z)

# creat our own unfun 
# def myadd(x,y) :
#     return x+y
# xyz = np.frompyfunc(myadd,2,1)
# print(xyz([1,2,3,4,5],[5,6,7,8,9]))



# def myadd(x,y,z) :
#     return x+y+z
# xyz = np.frompyfunc(myadd,3,1)
# print(xyz([1,2,3,4,5],[5,6,7,8,9],[10,11,12,13,14]))
# print(type(np.add))
# x = "Ayush"
# print(type(x))
# check if function is a unfunc or not by using the if else
# if type(np.subtract) == np.ufunc:
#     print('subtract is ufunc')
# else:
#     print('add is not ufunc')
# # ===============multiplication==========
# import numpy as np
# arr1 = np.array ([1,2,3,4,5,6])
# arr2 = np.array ([29,34,45,67,48,27])
# newarr = np.multiply(arr1,arr2)
# print("Multiplication is:",newarr)

# # ============divide===================
# arr1 = np.array ([1,2,3,4,5,6])
# arr2 = np.array ([29,34,45,67,48,27])
# newarr = np.divide(arr1,arr2)
# print("Division is:",newarr)

# print(type(np.add))
# print(type(np.subtract))
# print(type(np.multiply))
# print(type(np.divide))
# ===power================
arr1 = np.array ([1,2,3,4,5,6])
arr2 = np.array ([1,2,3,4,5,6])

newwar = np.power(arr1,arr2)
print("power is:",newwar)
# ========mod/ remainder ========
arr1 = np.array ([1,2,3,4,5,6])
arr2 = np.array ([1,2,3,4,5,6])

newwar = np.power(arr1,arr2)
print("Remainder is is:",newwar)
