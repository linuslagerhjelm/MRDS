
class Laser:
    def __init__(self, mrds):
        self.mrds = mrds

    def get_scan(self):
        return self.mrds.get_laser_echoes()

