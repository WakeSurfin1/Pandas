import json
import pandas as pd

# read json file to dictionary
with open('C:\mydata\colors.json') as data_file:    
    data = json.load(data_file)  
    
df = pd.DataFrame.from_dict(data)
print (df)