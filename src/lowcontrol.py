from src.laser import Laser
import utils
import math


class LowControl:
    """ Lowcontrol represents a planner for the tracker robot over on MRDS

        Attributes:
            linear    the current linear speed
            angular   the current angular speed
            mrds      a mrdsapi object that handles api requests
            laser     a laser object that handles laser data
    """
    def __init__(self, mrds):
        self.linear = None
        self.angular = None
        self.mrds = mrds
        self.laser = Laser(mrds)
        return

    def set_linear_speed(self, linear):
        """
            Updates both the planner and tracker linear speed, angular speed
            remains unchanged
        """
        self.linear = linear
        self.mrds.post_speed(self.angular, linear)

    def set_angular_speed(self, angular):
        """
            Updates both the planner and tracker angular speed, linear speed
            remains unchanged
        """
        self.angular = angular
        self.mrds.post_speed(angular, self.linear)

    def set_speed(self, angular, linear):
        """Updates both angular and linear speed for both planner and tracker"""
        self.linear = linear
        self.angular = angular
        self.mrds.post_speed(angular, linear)
    
    def steer_to_point(self, speed, curvature):
        """
            Receives speed and curvature and tells the robot to start
            the drive to a point
        """
        # omega = vY according to lecture notes
        omega = speed*curvature
        if self.laser.will_crash():
            omega *= 2
        self.set_speed(omega, speed)

    def get_location(self):
        """Returns a pose object for the robots current position"""
        return self.mrds.get_localization()

    def get_laser_scan(self):
        """Performs a laser scan on the robot and returns the result"""
        return self.mrds.get_laser_echoes()

    def reached_point(self, gp):
        """
            Uses the rules from the specification to determine if the
            robot has reached the specified point
        """
        p1 = self.mrds.get_localization()
        return utils.pos_dist(p1, gp) < 1

    def stop_robot(self):
        """Stops the robot"""
        self.set_speed(0, 0)
