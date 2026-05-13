import pandas as pd

# # df =pd.read_csv(r"C:\Users\NIELIT\Downloads\data (1).csv")
# # print(df.to_string())

# ir = pd.read_csv(r"C:\Users\NIELIT\Downloads\data (2).csv")
# print(ir)
# # =============json java script object nation=====================

# df = pd.read_json('http://www.w3school.com/python/pandas/data.js')
# print(df.to_string())

df = pd.read_json('https://www.w3schools.com/python/pandas/data.js')
print(df.head())
print(df.tail())

# # print("Hello worlds")
# df = pd.read_json('http://www.w3school.com/python/pandas/data.js')
# print(df.to_string())