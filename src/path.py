import json
from src.utils import *
from exception.NoAvailablePathException import NoAvailablePathException


class Path:
    # f should be the file containing the json path info
    def __init__(self, f):
        try:
            with open(f, 'r') as data_file:
                self.data_points = json.loads(data_file.read())

                # Reverse list to allow it to function as a stack
                self.data_points = list(self.data_points)
                data_file.close()

        except Exception:
            # Rethrow with custom exception for clarity
            raise NoAvailablePathException("Failed to read path file on path: " 
                    + f)



    def get_goal_point(self, lookahead, laser):
        """Returns an ideal goal point based on start point, lookahead distance 
        and latest laser scan"""
        # We are not choosing the correct goal point
        goal_point = self.data_points[0]
        for i in range(0, len(self.data_points)):
            dist = pos_dist(goal_point, self.data_points[i])
            if dist < lookahead:
                goal_point = self.data_points[i]
            else:
                if i <= 1:
                    self.data_points = self.data_points[i:]
                break

        return goal_point
