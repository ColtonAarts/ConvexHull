import Util as Util
import math
import numpy as np


class point_object:
    def __init__(self):
        self.polar = None
        self.cart = None

    def __str__(self):
        return str(self.polar) + " " + str(self.cart)

    def __repr__(self):
        return "("+str(self.polar) + ", " + str(self.cart) + ")"

    def set_polar(self, coords):
        self.polar = coords

    def set_cart(self, coords):
        self.cart = coords


def turn(point_one, point_two, point_three):
    # Find side a
    a = math.sqrt(point_one[0] ** 2 + point_two[0] ** 2 - (2*point_one[0]*point_two[0] *
                  math.cos(point_two[1] - point_one[1])))
    print("a = ")
    print(a)
    alpha = math.asin((point_one[0] * math.sin(point_two[1] - point_one[1])) / a)
    print("alpha = ")
    print(alpha)
    # alpha = math.asin(a/math.sin(point_two[1]-point_one[1]))
    b = math.sqrt(point_two[0] ** 2 + point_three[0] ** 2 - 2 * point_two[0] * point_three[0] *
                  math.cos(point_three[1] - point_two[1]))
    print("b = ")
    print(b)

    beta = math.asin((point_three[0] * math.sin(point_three[1]-point_two[1])) / b)
    print("beat = ")
    print(beta)
    # beta = math.asin(b/math.sin(point_three[1]-point_two[1]-point_three[1]))
    # print(alpha)
    # print(beta)
    print(abs(alpha) + abs(beta))
    if abs(alpha) + abs(beta) > math.pi:
        return 1
    else:
        return 0


def find_convex_hull(points):
    final_points = list()
    first_point = points[0]
    for ele in points:
        if ele[1] < first_point[1]:
            first_point = ele
    polar_coordinates = list()
    points.remove(first_point)
    # polar_coordinates.append(first_point)
    # print("first point = ")
    # print(first_point)
    for ele in points:
        # print(ele)
        point = point_object()
        point.set_cart(ele)
        if ele != first_point:
            new_point = (Util.change_origin_cartesian(first_point, ele))
            point.set_polar(Util.convert_to_polar(new_point))
            # print(new_point)
            polar_coordinates.append(point)
    # points = [x for _, x in sorted(zip(polar_coordinates, points), key=lambda s: s[1])]
    # print(points)
    polar_coordinates.sort(key=lambda x: x.polar[1])
    # print(polar_coordinates)

    for num in range(len(polar_coordinates)):
        print(polar_coordinates[num])
        while (len(final_points) > 1) and turn(final_points[1].polar, final_points[0].polar,
                                               polar_coordinates[num].polar) > 0:
            final_points.pop(0)
        final_points.insert(0, polar_coordinates[num])
        print(final_points)
    print(final_points)



    # for num in range(len(polar_coordinates)-1):
    #     if polar_coordinates[num][1] == polar_coordinates[num+1][1]:
    #         if polar_coordinates[num][0] > polar_coordinates[num+1][0]:
    #             polar_coordinates.pop[num+1]
    #         else:
    #             polar_coordinates.pop(num)




points = [(10, 1), (5, 5), (15, 18), (12, 3), (2, 2), (6, 17)]
find_convex_hull(points)
