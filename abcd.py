import pandas as pd 
# # pd.__version__
# # L= [14,15,96,99,87]
# # print(L)
# # ds = pd.Series(L)
# # print(ds)
# # print(ds[4])
# # Data = [1,2,3,4,5,6,7,8]
# # s = pd.DataFrame(Data)
# # print(s)
# # Data = [{'a':1, 'b': 2},{'a':5, 'b':10, 'c':20}]
# # df = pd.DataFrame(Data)
# # print(df)
# Data = {'name':['Tom','jack','steve','Ricky','Rohan','sohan'],
#         'Age':[28,34,29,42,35,36],
#         'Salry': [45000,32000,25000,62000,45000,32000]}
# df = pd.DataFrame(Data)
# print(df)
# # print(df.head)
# # print(df.tail)
# # print(df.rename(columns={"salary":"Monthly salary"}))
# # print(df.shape)
# # print(df.describe)
# # print(df.info)
# print(df.to_csv('Bhaisya.txt','index = False'))


print("Hello world")
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 