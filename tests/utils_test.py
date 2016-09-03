import unittest
from src.utils import Utils

P1 = {"Pose":{"Orientation":{"W":0.934419274330161,"X":5.202893838900563e-8,"Y":1.6770653061148675e-8,"Z":-0.35621511936231615},"Position":{"X":5.079651832580566,"Y":-3.4131758213043213,"Z":0.07760069519281387}},"Status":4,"Timestamp":91065}
P2 = {"Pose":{"Orientation":{"W":0.9344192743301392,"X":6.72200712870108e-8,"Y":1.1261678700691391e-8,"Z":-0.35621508955955505},"Position":{"X":5.079651832580566,"Y":-3.4131760597229004,"Z":0.07760068029165268}},"Status":4,"Timestamp":90876}
DISTANCE = 2.384185791015625e-07


class UtilsTest(unittest.TestCase):
    def test_position_equals(self):
        self.assertTrue(Utils.position_equals(P1, P1))

    def test_position_not_equals(self):
        self.assertFalse(Utils.position_equals(P1, P2))

    def test_position_distance(self):
        self.assertEquals(Utils.position_distance(P1, P2), DISTANCE)
