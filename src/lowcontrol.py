from src.laser import Laser
from time import sleep
from threading import Timer
import utils


class LowControl:
    """ Robot represents a planner for the tracker robot over on MRDS

        Attributes:
            linear    the current linear speed
            angular   the current angular speed
            mrds      a mrdsapi object that handles api requests
            laser     a laser object that handles laser data
            pose      a pose object representing the current location of the 
                      robot
    """
    def __init__(self, mrds):
        self.linear = None
        self.angular = None
        self.mrds = mrds
        self.timer = None
        self.laser = Laser(mrds)
        self.pose = self.mrds.get_localization()
        return

    def set_linear_speed(self, linear):
        """Updates both the planner and tracker linear speed, angular speed 
           remains unchanged"""
        self.linear = linear
        self.mrds.post_speed(self.angular, linear)

    def set_angular_speed(self, angular):
        """Updates both the planner and tracker angular speed, linear speed 
            remains unchanged"""
        self.angular = angular
        self.mrds.post_speed(angular, self.linear)

    def set_speed(self, angular, linear):
        """Updates both angular and linear speed for both planner and tracker"""
        self.linear = linear
        self.angular = angular
        self.mrds.post_speed(angular, linear)
    
    def steer_to_point(self, point, speed, rotation):
        # if self.timer:
        #    self.timer.cancel()

        loc = self.mrds.get_localization()
        dist = utils.position_distance(loc, point)
        # rot = utils.degree_distance(loc, point)

        timeout = dist/speed

        self.set_speed(0, speed)
        # self.timer = Timer(timeout, self._stop_robot)
        # self.timer.start()

    def _stop_robot(self):
        self.set_speed(0, 0)
        self.timer = None
