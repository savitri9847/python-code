# import numpy as np

# Array_2D = np.array([[1, 2, 3], [4, 5, 6]])
# print(Array_2D)
# if 5 > 2:
#   print("Five is greater than two!")

class A:
    
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        obj = B()
        obj.show()
        

        