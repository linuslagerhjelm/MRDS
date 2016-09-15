
class Laser:
    def __init__(self, mrds):
        self.mrds = mrds

    def get_scan(self):
        return self.mrds.get_laser_echoes()

    def will_crash(self):
        laser_scan = get_scan()
        ang= len(laser_scan)
        for i in range(-2,2):
            if laser_scan[ang/2 + i] < 0.5:
                return true
        return false
