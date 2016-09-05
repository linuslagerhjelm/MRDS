import unittest
from src.lowcontrol import LowControl
from src.mrdsapi import Mrdsapi

P1 = {"Pose":{"Orientation":{"W":0.9999560713768072,"X":0.000001257266799023306,"Y":4.498194444970086e-8,"Z":-0.010503618049016405},"Position":{"X":-0.0038328170776367188,"Y":0.00782086607068777,"Z":0.07760074734687805}},"Status":4,"Timestamp":30715}
ADDRESS = "localhost"
PORT = 50000


class LowControlTest(unittest.TestCase):
    def test_steer_to_point(self):
        mrds = Mrdsapi(ADDRESS, PORT)
        lc = LowControl(mrds)
        lc.steer_to_point(P1, 1)
