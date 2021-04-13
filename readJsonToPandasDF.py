### import json into pandas dataframe
import pandas as pd
pd.set_option('max_colwidth', 800)

inputFile = 'C:\mydata\devices.json'

df = pd.read_json (inputFile)
print(df)

## input data size and data types
cntRecs = df.shape[0]  # number of records
cntCols = df.shape[1]  # number of columns

print("num records = " + str(cntRecs))
print("num columns = " + str(cntCols))