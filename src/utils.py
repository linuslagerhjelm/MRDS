import json
import math
from src.given import heading


def pos_dist(p1, p2):
    """Returns the euclidean distance between two points as a floating point 
        value"""
    pos1 = p1["Pose"]["Position"]
    pos2 = p2["Pose"]["Position"]
    
    # Omit the Z coordinates as suggested by supervisor
    return math.sqrt(((pos1["X"] - pos2["X"])**2) + ((pos1["Y"] - pos2["Y"])**2))


def delta_x(p1, p2):
    x1= p1["Pose"]["Position"]["X"]
    x2= p2["Pose"]["Position"]["X"]
    return math.fabs(x1-x2)


def delta_y(p1, p2):
    y1 = p1["Pose"]["Position"]["Y"]
    y2 = p2["Pose"]["Position"]["Y"]
    return math.fabs(y1-y2)


def norm_y_dist(loc, gp):
    dist = pos_dist(loc, gp)
    w = heading(loc["Pose"]["Orientation"])
    angle_rcs_y = math.atan2(delta_y(loc, gp), delta_x(loc, gp))
    angle_wcs_y = angle_rcs_y - math.atan2(w["Y"], w["X"])
    # print math.cos(new_angle) * 180 / math.pi
    return math.sin(angle_wcs_y)*dist


def norm_y(robot_p, p):
    """Convert a x position in RCS to WCS"""
    x_prim = p["Pose"]["Position"]["X"]
    y_prim = p["Pose"]["Position"]["Y"]
    y0 = robot_p["Pose"]["Position"]["Y"]
    w = p["Pose"]["Position"]["W"]
    return y0 + x_prim*math.sin(w) - y_prim*math.cos(w)


def norm_x(robot_p, p):
    """Convert a y position in RCS to WCS"""
    x_prim = p["Pose"]["Position"]["X"]
    y_prim = p["Pose"]["Position"]["Y"]
    x0 = robot_p["Pose"]["Position"]["X"]
    w = p["Pose"]["Position"]["W"]
    return x0 + x_prim * math.cos(w) - y_prim * math.sin(w)


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
