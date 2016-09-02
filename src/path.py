import sys
import logging
import json

class Path:
    #f should be the file containing the json path info
    def __init__ (self, f):
        try:
            with open(f,'r') as data_file:
                self.data = (data_file.read())
                self.json_data = json.loads(self.data)
                data_file.close()
        except TypeError:
            raise (NoAvailablePathException("Failed to read path file"))

    def get_closest_pos(self, loc):
        return null
    def get_goal_point(self, start, lookahead, laser):
        return null 

