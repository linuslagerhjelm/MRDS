import math
from src.given import heading


def pos_dist(p1, p2):
    """
        Returns the euclidean distance between two points as a floating point
        value
    """
    pos1 = p1["Pose"]["Position"]
    pos2 = p2["Pose"]["Position"]
    
    # Omit the Z coordinates as suggested by supervisor
    return math.sqrt(((pos1["X"] - pos2["X"])**2) + ((pos1["Y"] - pos2["Y"])**2))


def delta_x(p1, p2):
    """ Returns x distance between two points """
    x1 = p1["Pose"]["Position"]["X"]
    x2 = p2["Pose"]["Position"]["X"]
    return x1-x2


def delta_y(p1, p2):
    """ Returns y distance between two points """
    y1 = p1["Pose"]["Position"]["Y"]
    y2 = p2["Pose"]["Position"]["Y"]
    return y1-y2


def rcs_y_dist(loc, gp):
    """ Returns the RCS y distance between two points in the WCS system """
    dist = pos_dist(loc, gp)
    w = heading(loc["Pose"]["Orientation"])
    angle_wcs = math.atan2((delta_y(gp, loc)), (delta_x(gp, loc)))
    angle_w = math.atan2((w["Y"]), (w["X"]))
    if angle_wcs > math.pi:
        angle_wcs = 2*math.pi - angle_wcs
    if angle_wcs < math.pi:
        angle_wcs = 2*math.pi + angle_wcs
    if angle_w > math.pi:
        angle_w = 2*math.pi - angle_w
    if angle_w < math.pi:
        angle_w = 2*math.pi + angle_w
    angle_wcs -= angle_w
    # print math.cos(new_angle) * 180 / math.pi
    return math.sin(angle_wcs)*dist


def norm_y(robot_p, p):
    """ Convert a x position in RCS to WCS """
    x_prim = p["Pose"]["Position"]["X"]
    y_prim = p["Pose"]["Position"]["Y"]
    y0 = robot_p["Pose"]["Position"]["Y"]
    w = p["Pose"]["Position"]["W"]
    return y0 + x_prim*math.sin(w) - y_prim*math.cos(w)


def norm_x(robot_p, p):
    """ Convert a y position in RCS to WCS """
    x_prim = p["Pose"]["Position"]["X"]
    y_prim = p["Pose"]["Position"]["Y"]
    x0 = robot_p["Pose"]["Position"]["X"]
    w = p["Pose"]["Position"]["W"]
    return x0 + x_prim * math.cos(w) - y_prim * math.sin(w)


def y_dist(p1, p2):
    w1 = p1["Pose"]["Position"]["W"]
    x1 = p1["Pose"]["Position"]["X"]
    y1 = p1["Pose"]["Position"]["Y"]
    w2 = p2["Pose"]["Position"]["W"]
    x2 = p2["Pose"]["Position"]["X"]
    y2 = p2["Pose"]["Position"]["Y"]
    
    return math.fabs(p2["Pose"]["Position"]["Y"] - p1["Pose"]["Position"]["Y"])
