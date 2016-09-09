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
        self.speed = speed

    def start(self, path):
        """ Makes the robot follow the given path using the pure pursuit 
            algorithm
        """

        # Define a goal point (GP) on the path, at distance L from the robot
        gp = path.get_goal_point(self.look, self.lc.get_laser_scan())
        print self.lc.get_location()
        print gp
        i = 1
        #len(path.data_points)
        while True:
            loc = self.lc.get_location()

            if self.lc.reached_point(gp):
                # Define a goal point (GP) on the path, at distance L from the robot
                print "New GP!"
                i = -i
                gp = path.get_goal_point(self.look, self.lc.get_laser_scan())

            lookahead = utils.pos_dist(gp, loc)

            # Construct a circle passing through (0,0)RCS and GP, such that the
            # vehicle orientation is a tangent to the circle The circle is defined
            # by its radius r and midpoint We know that r = L^2/2y from geometry
            y = utils.norm_y_dist(loc, gp)

            r = (lookahead**2) / (2*y)
            # Set phi or omega to correspond to motion along this circle, omega = vY
            # where v is the linear speed and Y=1/r is the curvature of the circle
            v = self.speed
            Y = 1/r
            self.lc.steer_to_point(self.speed, Y)

            # sleep briefly to prevent socket overload
            sleep(0.001)

        return
