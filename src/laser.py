
class Laser:
    def __init__(self, mrds):
        self.mrds = mrds

    def get_scan(self):
        return self.mrds.get_laser_echoes()["Echoes"]

    def will_crash(self):
        """Returns if the robot is about to collide into a wall, returns -1 if it's
            about to collide to the right, 0 if it's not about to collide and 1
            if it's about to collide to the left"""
        laser_scan = self.get_scan()
        ang = len(laser_scan)
        # -8, -1 is to the right of the robot
        for i in range(-10, 10):
            if laser_scan[int(round(ang/2) + i)] < .6:
                return True
        # 0, 8 is to the left of the robot
        return False
