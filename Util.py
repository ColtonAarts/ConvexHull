import math


def convert_to_polar(point):
    r = math.sqrt(point[0] ** 2 + point[1] ** 2)
    theta = math.atan(point[1] / point[0])
    if point[0] < 0:
        theta += math.pi
    elif point[0] > 0 and point[1] < 0:
        theta += 2 * math.pi
    return r, theta


def change_origin_polar(point_a, point_b):
    new_r = math.sqrt(point_a[0]**2 + point_b[0]**2 - (2 * point_a[0] * point_b[0] * math.cos(point_b[1] - point_a[1])))
    new_theta = math.asin((point_b[0] / new_r) * math.sin((point_b[1] - point_a[1])))
    return new_r, new_theta


def change_origin_cartesian(new_origin, other_point):
    new_x = other_point[0] - new_origin[0]
    new_y = other_point[1] - new_origin[1]
    return new_x, new_y


def angle(origin, point):
    point = change_origin_cartesian(origin, point)
    h = math.sqrt(point[0]**2 + point[1]**2)
    return math.sin(point[1]/h)


def orientation(p1, p2, p):
    orin = (p2[0] - p1[0]) * (p[1] - p1[1]) - (p[0] - p1[0]) * (p2[1] - p1[1])
    if orin < 0:
        return -1
    elif orin > 0:
        return 1
    else:
        return 0

