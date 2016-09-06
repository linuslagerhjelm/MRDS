from time import sleep
from threading import Timer
import utils


class HighControl:
    """ Highcontrol represents a planner for the tracker robot over on MRDS

        Attributes:
    """
    def __init__(self, lowcontrol, lookahead, speed):
        self.lc = lowcontrol
        self.look = lookahead
        self.path = path
        self.speed = speed

    def start(self, path):
        """ Makes the robot follow the given path using the pure pursuit 
            algorithm
        """
        loc = self.lc.get_location()

        # Define a goal point (GP) on the path, at distance L from the robot
        gp = self.path.get_goal_point(self.path.get_closest_pos(),
                self.look, loc, self.lc.get_laser_scan())

        # Construct a circle passing through (0,0)RCS and GP, such that the
        # vehicle orientation is a tangent to the circle The circle is defined
        # by its radius r and midpoint We know that r = L^2/2y from geometry  
        y = utils.get_y_dist(gp,loc)
        r = (gp**2) / (2*y)

        # Set phi or omega to correspond to motion along this circle, omega = vY
        # where v is the linear speed and Y=1/r is the curvature of the circle
        v = self.speed
        Y = 1/r

        self.lc.steer_to_point(gp,self.speed,Y)

        return
