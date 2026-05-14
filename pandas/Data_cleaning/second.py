
import pandas as pd
df =pd.read_csv(r"\\pc-208\E\Ayush Kumar Sain\data (2).csv")
# print("original read",df.to_string())
# dd/mm/yyyy
df['Date'] = pd. to_datetime(df['Date'],format= 'mixed')
# mm/dd/yyyy
df['Date'] = df['Date'].dt.strftime('%m/%d/%y')
# print(df.to_string())
df.loc[7,'Duration'] = 4
# df.loc[18,'calories'] =356.5
df.loc[[7,5,3,10,4],'Duration'] =45
print(df.to_string())
