import json
import math
from Quaternion import normalize
from Quaternion import Quat


def position_equals(p1, p2):
    """Compares two points to determine if the are the same"""
    return json.dumps(p1) == json.dumps(p2)


def pos_dist(p1, p2):
    """Returns the euclidean distance between two points as a floating point 
        value"""
    pos1 = p1["Pose"]["Position"]
    pos2 = p2["Pose"]["Position"]
    
    # Omit the Z coordinates as suggested by supervisor
    return math.sqrt(((pos1["X"] - pos2["X"])**2) +
            ((pos1["Y"] - pos2["Y"])**2))

def delta_x(p1,p2):
    x1= p1["Pose"]["Position"]["X"]
    x2= p2["Pose"]["Position"]["X"]
    return math.fabs(x1-x2)

def delta_y(p1,p2):
    y1= p1["Pose"]["Position"]["Y"]
    y2= p2["Pose"]["Position"]["Y"]
    return math.fabs(y1-y2)

def norm_dist(p1,p2):
    dist = pos_dist(p1,p2)
    w = p["Pose"]["Position"]["W"]
    angle = math.atan2(delta_x(p1,p2),delta_y(p1,p2))
    new_angle = math.pi/4 - angle - w
    return sin(new_angle)*dist


def norm_y(robot_p, p):
    """Convert a x position in RCS to WCS"""
    xPrim = p["Pose"]["Position"]["X"]
    yPrim = p["Pose"]["Position"]["Y"]
    y0 = robot_p["Pose"]["Position"]["Y"]
    w = p["Pose"]["Position"]["W"]
    return y0 + xPrim*math.sin(w) - yPrim*math.cos(w)

def norm_x(robot_p, p):
    """Convert a y position in RCS to WCS"""
    xPrim = p["Pose"]["Position"]["X"]
    yPrim = p["Pose"]["Position"]["Y"]
    x0 = robot_p["Pose"]["Position"]["X"]
    w = p["Pose"]["Position"]["W"]
    return x0 + xPrim*math.cos(w) - yPrim*math.sin(w)

def x_dist(p1, p2):
    return math.fabs(p2["Pose"]["Position"]["X"] - p1["Pose"]["Position"]["X"])



def y_dist(p1, p2):
    w1 = p1["Pose"]["Position"]["W"]
    x1 = p1["Pose"]["Position"]["X"]
    y1 = p1["Pose"]["Position"]["Y"]
    w2 = p2["Pose"]["Position"]["W"]
    x2 = p2["Pose"]["Position"]["X"]
    y2 = p2["Pose"]["Position"]["Y"]
    
    return math.fabs(p2["Pose"]["Position"]["Y"] - p1["Pose"]["Position"]["Y"])


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
