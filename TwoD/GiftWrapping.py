import random
import Util
import math


def find_convex_hull(points):
    final_points = list()
    current_point = points[0]
    final_point = None
    next_point = points[random.randint(1, len(points) - 1)]

    for ele in range(len(points)):
        if points[ele][0] < current_point[0]:
            current_point = points[ele]
    first_point = current_point
    final_points.append(current_point)
    while final_point != first_point:
        for ele in range(len(points)):
            if points[ele] != next_point and points[ele] != current_point:
                if Util.orientation(current_point, next_point, points[ele]) == 1:
                    next_point = points[ele]

        final_point = next_point
        final_points.append(next_point)
        current_point = next_point
        rand_num = random.randint(1, len(points) - 1)
        next_point = points[rand_num]
    return final_points

