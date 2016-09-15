from time import sleep
import math
import utils


class HighControl:
    """ Highcontrol represents a planner for the tracker robot over on MRDS

        Attributes:
            lc: a Lowcontrol object used to send commands to the robot
            look: the user specified value for the lookahead
            speed: the user specified value for the linear speed
    """
    def __init__(self, lowcontrol, lookahead, speed):
        self.lc = lowcontrol
        self.look = lookahead
        self.speed = speed

    def start(self, path):
        """ Makes the robot follow the given path using the pure pursuit 
            algorithm
        """

        gp = self.lc.get_location()
        while not self._has_reached_goal(path):
            loc = self.lc.get_location()

            # Define a goal point (GP) on the path, at distance L from the robot (if we reached the previous one)
            if self.lc.reached_point(gp):
                gp = path.get_goal_point(self.look, self.lc.get_laser_scan())


            self.lc.steer_to_point(loc, gp, self.speed)

            # sleep briefly to prevent socket overload
            sleep(0.05)

        self.lc.stop_robot()

    def _has_reached_goal(self, path):
        """Determines weather the robot has reached the goal on the path"""
        if not path.past_half(): return False
        return self.lc.reached_point(path.get_final_point())
