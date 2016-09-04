import json
import math

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
        # o1 = p1["Pose"]["Orientation"]
        # o2 = p2["Pose"]["Orientation"]
        return None
