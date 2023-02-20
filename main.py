import logic
import json

import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
#sys.path.append(parent)
 
new = os.path.join(current, 'Data\\ICRI_Envirosensor_Data')

# Opening JSON file
f = open('C:\\workspace\\mongo\\Data\\ICRI_Envirosensor_Data\\aaa_iot.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

deviceId = data[0]["deviceId"]
data_payload = data[0]["data"]
data_payload = data_payload[:-1]

#This prints out the value of the data field into a json format 
print(deviceId)
print(data_payload)
  
# Iterating through the json
# list
for i in data:

    keys = i.keys()
    values = i.values()
    #Put something here to write this to a mongoDB call
    #print(keys)
    #print(values) 
  
# Closing file
f.close()