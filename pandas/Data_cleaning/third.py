import pandas as pd 
# import the file and read the data
# it consists of some duplicate values
df = pd.read_csv (r"C:\Users\NIELIT\Downloads\data (2).csv")
# print("original read",df.to_string())
print("Showing the duplicate value:",df.duplicated())

df.drop_duplicates(inplace =True)
print("After the removing the duplicated value:",df.to_string())