import json

inputFile = 'C:\mydata\colors.json'

# Opening JSON file
f = open(inputFile)
  
# load json file into a list of dictionaries
data = json.load(f)
#print(len(data))
#print(type(data))

# loop thru objects / dictionaries nested in 'colors'
for i in data['colors']:
    #print(len(i))
    
    for key, value in i.items():
        
        parentKey = key
        
        if type(value) == str:
             print(key, ':', value)
                
        # if nested dictionary, ouput each        
        elif type(value) == dict:
            
            for key, value in value.items():
                
                if type(value) == str:
                    print(parentKey, ':', key, ':', value)
                
                # if nested list, output each
                elif type(value) == list:    
                    for j in value:
                        print(parentKey, ':', key, '->', j)
        else:
            print("type out of scope")

    print("<EOL>")    
    
# Closing file
f.close()