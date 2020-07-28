import matplotlib.pyplot as plt
from TwoD import GiftWrapping
import numpy as np

N = 100
r0 = 0.6
x = np.random.rand(N)
y = np.random.rand(N)

test_points = list()
for ele in range(len(x)):
    test_points.append((x[ele], y[ele]))

for point in test_points:
    plt.plot(point[0], point[1], 'ko')

convexHull = GiftWrapping.find_convex_hull(test_points)

for point in range(len(convexHull)):
    plt.plot(convexHull[point][0], convexHull[point][1], 'ro')

    if point == (len(convexHull) - 1):
        plt.plot([convexHull[point][0], convexHull[0][0]], [convexHull[point][1], convexHull[0][1]], 'r--')
    else:
        plt.plot([convexHull[point][0], convexHull[point + 1][0]], [convexHull[point][1], convexHull[point + 1][1]],
                 'r--')

plt.show()

