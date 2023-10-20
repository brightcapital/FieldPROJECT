import pandas as pd



data1 = pd.read_csv('bloomberg_price.csv')
data2 = pd.read_csv('bloomberg_curr.csv')

data_combined = pd.concat([data2,data1],axis=0)

data_combined.to_csv('bloomberg_data.csv',index=False)