import json
from src.utils import *
from exception.NoAvailablePathException import NoAvailablePathException


class Path:
    def __init__(self, f):
        try:
            with open(f, 'r') as data_file:
                self.data_points = json.loads(data_file.read())
                self.data_points = list(self.data_points)
                self.goal = self.data_points[-1]
                self.initial_length = len(self.data_points)
                data_file.close()

        except Exception:
            # Rethrow with custom exception for clarity
            raise NoAvailablePathException("Failed to read path file on path: " + f)

    def get_goal_point(self, lookahead, laser):
        """Returns an ideal goal point based on lookahead distance
        and latest laser scan"""
        goal_point = self.data_points[0]
        for i in range(1, len(self.data_points)):
            dist = pos_dist(goal_point, self.data_points[i])
            if dist > lookahead:
                goal_point = self.data_points[i]
                self.data_points = self.data_points[i+1:]
                break

        return goal_point

    def past_half(self):
        return len(self.data_points) <= (self.initial_length/2)

    def get_final_point(self):
        return self.goal
