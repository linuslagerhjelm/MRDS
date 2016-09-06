import json
import math
from Quaternion import normalize
from Quaternion import Quat


def position_equals(p1, p2):
    """Compares two points to determine if the are the same"""
    return json.dumps(p1) == json.dumps(p2)


def position_distance(p1, p2):
    """Returns the euclidean distance between two points as a floating point 
        value"""
    pos1 = p1["Pose"]["Position"]
    pos2 = p2["Pose"]["Position"]
    
    # Omit the Z coordinates as suggested by supervisor
    return math.sqrt(((pos1["X"] - pos2["X"])**2) +
            ((pos1["Y"] - pos2["Y"])**2))


def get_x_dist(p1, p2):
    return p2["Pose"]["Position"]["X"] - p1["Pose"]["Position"]["X"]


def get_y_dist(p1, p2):
    return p2["Pose"]["Position"]["Y"] - p1["Pose"]["Position"]["Y"]


def degree_distance(p1, p2):
    pos1 = p1["Pose"]["Orientation"]
    pos2 = p2["Pose"]["Orientation"]
    n1 = normalize([pos1["X"], pos1["Y"], pos1["Z"], pos2["W"]])
    n2 = normalize([pos2["X"], pos2["Y"], pos2["Z"], pos2["W"]])
    ang1 = 2 * math.acos(n1[3])
    ang2 = 2 * math.acos(n2[3])

    return ang2 - ang1

    # return math.acos(
    #        (2*(n1[0]*n2[0]+n1[1]*n2[1]+n1[2]*n2[2]+n1[3]*n2[3])**2)-1)
