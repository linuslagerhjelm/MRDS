import json
import math
from Quaternion import Quat
from Quaternion import normalize

class Utils:


    @staticmethod
    def position_equals(p1, p2):
        """Compares two points to determine if the are the same"""
        return json.dumps(p1) == json.dumps(p2)

    @staticmethod
    def position_distance(p1, p2):
        """Returns the euclidean distance between two points as a floating point value"""
        pos1 = p1["Pose"]["Position"]
        pos2 = p2["Pose"]["Position"]

        # Omit the Z coordinates as suggested by supervisor
        return math.sqrt(((pos1["X"] - pos2["X"])**2) + ((pos1["Y"] - pos2["Y"])**2))

    @staticmethod
    def degree_distance(p1, p2):
        pos1 = p1["Pose"]["Orientation"]
        pos2 = p2["Pose"]["Orientation"]
        n1 = normalize([pos1["X"], pos1["Y"], pos1["Z"], pos2["W"]])
        n2 = normalize([pos2["X"], pos2["Y"], pos2["Z"], pos2["W"]])
        
        # angle = arccos(2*(a1a2+b1b2+c1c2+d1d2)^2-1)
        ang = math.acos((2*
                (n1[0]*n2[0]+n1[1]*n2[1]+n1[2]*n2[2]+n1[3]*n2[3])**2)-1)

        # o1 = p1["Pose"]["Orientation"]
        # o2 = p2["Pose"]["Orientation"]
        return ang
