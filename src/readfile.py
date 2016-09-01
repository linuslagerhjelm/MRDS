import sys
import json


try:
    with open(sys.argv[1],'r') as data_file:
        data = (data_file.read())
        json_data = json.loads(data)
        # print (json_data['pose'])
        data_file.close()
except TypeError:
        print ("ERROR: Unable to read file")

