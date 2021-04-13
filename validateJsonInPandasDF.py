### import json into pandas dataframe and check the data
import pandas as pd
pd.set_option('max_colwidth', 800)

inputFile = 'C:\mydata\devices.json'
minRecs = 1
maxRecs = 500000
targetCols = 2
minPrice = .01
maxPrice = 10000

df = pd.read_json (inputFile)
#print(df)

## input data size and data types
cntRecs = df.shape[0]  # number of records
cntCols = df.shape[1]  # number of columns

if not minRecs <= cntRecs <= maxRecs:
    print("ERROR: input data record count out of scope " + str(cntRecs))

if cntCols != targetCols:
    print("ERROR: number input columns" + str(cntCols) + " != number target columns " + str(targetCols))

if str((df['Price'].dtypes)) != 'int64':
    print("ERROR: input attribute has invalid data type")

## loop through each record
## check column values
for index, record in df.iterrows():
    if not minPrice <= record['Price'] <= maxPrice:
        print("ERROR: Price value incorrect " + str(record['Price']))

exit(1)