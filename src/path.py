import json
from src.utils import Utils
from exception.NoAvailablePathException import NoAvailablePathException


class Path:
    # f should be the file containing the json path info
    def __init__(self, f):
        try:
            with open(f, 'r') as data_file:
                self.data_points = json.loads(data_file.read())

                # Reverse list to allow it to function as a stack
                self.data_points = list(reversed(self.data_points))
                data_file.close()

        except Exception:
            # Rethrow with custom exception for clarity
            raise NoAvailablePathException("Failed to read path file on path: " 
                    + f)

    def get_closest_pos(self):
        """Returns the closest Pose on the path"""
        return self.data_points.pop()

    def get_goal_point(self, start, loc, lookahead, laser):
        """Returns an ideal goal point based on start point, lookahead distance 
        and latest laser scan"""
        # while current look in list < lookahead distance
        #   get angle between robot (facing direction) and path
        #   find the corresponding laser(s) scan
        #   if laser scan distance is smaller than distance between robot and 
        #   point
        #       the point is behind something, return the previous point
        #   else look for the next point

        # NOTE: code somewhere else will have to check how close we must follow 
        #       the path in order to reach the goal point without crashing

        # NOTE2: we will have to add some handling for the "special" case where 
        #        our goal is the last point in the list. Aka we'll run out of 
        #        elements to pop from the list
        i = 0
        previous_point = start
        goal_point = self.data_points.pop()

        while i <= lookahead:
            deg = Utils.degree_distance(loc, goal_point)
            laser_dist = laser[deg]
            if laser_dist < Utils.position_distance(loc, goal_point):
                return previous_point
            else:
                i += 1
                previous_point = goal_point
                goal_point = self.data_points.pop()

        return goal_point
