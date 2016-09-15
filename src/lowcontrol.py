from laser import Laser
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
    
    def steer_to_point(self, loc, gp, speed):
        """
            Receives speed and curvature and tells the robot to start
            the drive to a point
        """
        L = utils.pos_dist(loc, gp)

        # Construct a circle passing through (0,0)RCS and GP, such that the
        # vehicle orientation is a tangent to the circle The circle is defined
        # by its radius r and midpoint We know that r = L^2/2y from geometry
        y = utils.rcs_y_dist(loc, gp)
        r = (L ** 2) / (2 * y)

        # Set phi or omega to correspond to motion along this circle, omega = vY
        # where v is the linear speed and Y=1/r is the curvature of the circle
        Y = 1 / r
        s = speed

        # sleep briefly to prevent socket overload
        # omega = vY according to lecture notes
        omega = s*Y

        crash = self.laser.will_crash()
        # Is about to crash on the right
        if crash == -1 or crash == 1:
            s = 0
        if utils.angle_dist(loc, gp) > math.pi:
            s = .2
            omega *= 100
        self.set_speed(omega, s)

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
        return utils.pos_dist(p1, gp) < .4

    def stop_robot(self):
        """Stops the robot"""
        self.set_speed(0, 0)
