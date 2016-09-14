import json
from src.utils import *
from src.given import heading
from exception.NoAvailablePathException import NoAvailablePathException


class Path:
    """ Path represents a path that consists of a series of Pose objects

            Attributes:
                data_points: a list of pose objects representing the path
                goal: the final point on the map
                initial_length: the original pose count in the list
        """
    def __init__(self, f):
        try:
            with open(f, 'r') as data_file:
                self.data_points = json.loads(data_file.read())
                self.data_points = list(self.data_points)
                data_file.close()
        except Exception:
            # Rethrow with custom exception for clarity
            raise NoAvailablePathException("Failed to read path file on path: " + f)

        self.goal = self.data_points[-1]
        self.initial_length = len(self.data_points)

    def get_goal_point(self, lookahead, laser):
        """
            Returns an ideal goal point based on lookahead distance
            and latest laser scan
        """
        init_point = self.data_points[0]
        goal_point = init_point
        for i in range(1, len(self.data_points)):
            dist = pos_dist(goal_point, self.data_points[i])
            if dist > lookahead:
                goal_point = self.data_points[i]
                self.data_points = self.data_points[i+1:]
                break

        # When we have found the optimal goal point, we want to
        # continue look ahead in our list and see if there is
        # another point, further ahead, that is also inside our
        # lookahead distance. This point will also need to have
        # much the same heading as the robot If such a point is
        # found, use the laser scan to determine if we can see it.
        # If we can we should pick that point instead. Else, use
        # the first point
        # for i in range(1, len(self.data_points)):
        #     dist = pos_dist(init_point, self.data_points[i])
        #     if dist < 2*lookahead:
        #         break

        return goal_point

    def past_half(self):
        """ Determines weather the robot has completed more than half the path """
        return len(self.data_points) <= (self.initial_length/2)

    def get_final_point(self):
        """ Returns the final point on the path """
        return self.goal
