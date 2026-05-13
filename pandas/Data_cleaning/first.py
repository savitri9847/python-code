# first day of Data claening using pandas 
# Data cleaning is the process of clearing the data 

# ===========What can be the bad data?==============
# missing value 
# Duplicate value 
# Empty cell 
# Empty Rows 
# Empty columns 
# wrong data type 
# inconsistent data 
# https://www.w3schools.com/python/pandas/data.js

import pandas as pd
# df = pd.read_csv(r"https://www.w3schools.com/python/pandas/data.js")
# # print(df.to_string())
# new_df =df.dropna()
# print(new_df.to_string)
# df.dropna()
# print(df.to_string)

# Adding the value in the empty cells===========

# dev = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")

# dev.fillna(258.5,inplace = True)
# print("After filling empty cells:", dev.to_string())
# filling the missing values with the different values

dev = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# dev.fillna({"calories":540.5},inplace= True)
# print("After filling empty cells with diffrent values:", dev.to_string())

# dev.loc[3, "Calories"] =123.5
# print("After filling empty cells:", dev.to_string())

# mean/median/mode=============================
# dev = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# x = dev["Calories"].mean()
# print("The mean value is:", x)

# dev.fillna({"Calories" : x}, inplace= True)
# print(dev.to_string())
# ================median====================================
# dev = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# x = dev["Calories"].median()
# print("The mean value is:", x)

# dev.fillna({"Calories" : x}, inplace= True)
# print(dev.to_string())
# ===========mode=======================================
dev = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
x = dev["Calories"].mode()[0]
print("The mean value is:", x)

dev.fillna({"Calories" : x}, inplace= True)
print(dev.to_string())