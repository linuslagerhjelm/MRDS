import sys
import json

class Path:
    #f should be the file containing the json path info
    def __init__ (self, f):
        try:
            with open(f,'r') as data_file:
                data = (data_file.read())
                self.json_data = json.loads(data)
                print(json.dumps(self.json_data))
                # print(json_data)
                # print (json_data['pose'])
                data_file.close()
        except TypeError:
            print ("ERROR: Unable to read file")

