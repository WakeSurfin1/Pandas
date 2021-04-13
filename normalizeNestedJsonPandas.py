import json
import pandas as pd
pd.set_option('max_colwidth', 800)

# read json file to python dictionary
with open('C:\mydata\colors.json') as data_file:    
    data = json.load(data_file)  
    
## create base df from members nested in colors array
df = pd.json_normalize(data, 'colors')

## create new dataframe with color and code.rgba nested object / array
df2 = df.filter(['color','code.rgba'], axis=1)

## create a new, empty dataframe
column_names = ['color']
df3 = pd.DataFrame(columns = column_names)

## loop through previous dataframe and append to new dataframe
for index, record in df2.iterrows():
    parentcol = record['color']
    
    ## get each member of the code.rgba array
    for i in record['code.rgba']:
        childcol = i
        ## populate the new dataframe with color and code.rgba value
        df3 = df3.append({'color': parentcol, 'code.rgba':childcol}, ignore_index=True)       
        
## drop column code.rgba from orig dataframe
df4 = df.drop('code.rgba', axis=1)

# join df4 and df3 by color
df5 = df4.set_index('color').join(df3.set_index('color'))
print(df5)