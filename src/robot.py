import Mrdsapi
import Conf
import Laser
import json

class Robot:

    def __init__(self, mrds):
        self.mrds = mrds
        self.laser = Laser()
        # pose['Pose']['Position]['X']
        self.pose = self.mrds.getLocalization()
        return

    def set_linear_speed(self,linear):
        self.linear = linear
        self.mrds.post_speed(self.angular, linear)

    def set_angular_speed(self,angular):
        self.angular= angular
        self.mrds.post_speed(angular, self.linear)

    def set_speed(self,angular,linear):
        self.linear = linear
        self.angular= angular
        self.mrds.post_speed(angular, linear)
    

