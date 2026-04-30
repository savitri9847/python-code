import pandas as pd
# mydataset = {
#     'cars': ["BMW", "Volvo","Ford"],
#     'passing': [3,7,2]
    
# }
# myvar =pd.DataFrame(mydataset)
# print(myvar)
# print("The version is:",pd.__version__)
a = [1,2,3,4,5,6]
Anothervar =pd.Series(a)

# print(Anothervar)
# print(type(Anothervar))
# print(Anothervar[0])

a = [1,2,3,4]
Zero = pd.Series(a, index= ["x","y","z","w"])
print(Zero)
print("Findig out the value :" ,Zero["z"])
