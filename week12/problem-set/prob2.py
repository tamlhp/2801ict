import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
# Stores the result (points of convex hull)
hull = set()
 
# Returns the side of point p with respect to line
# joining points p1 and p2.
def findSide(p1, p2, p):
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
 
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0
 
# returns a value proportional to the distance
# between the point p and the line joining the
# points p1 and p2
def lineDist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
            (p2[1] - p1[1]) * (p[0] - p1[0]))
 
# End points of line L are p1 and p2. side can have value
# 1 or -1 specifying each of the parts made by the line L
def quickHull(points, p1, p2, side):
    n = len(points)
    ind = -1
    max_dist = 0
 
    # finding the point with maximum distance
    # from L and also on the specified side of L.
    for i in range(n):
        temp = lineDist(p1, p2, points[i])
         
        if (findSide(p1, p2, points[i]) == side) and (temp > max_dist):
            ind = i
            max_dist = temp
 
    # If no point is found, add the end points
    # of L to the convex hull.
    if ind == -1:
        hull.add(p1)
        hull.add(p2)
        return
 
    # Recur for the two parts divided by a[ind]
    quickHull(points, points[ind], p1, -findSide(points[ind], p1, p2))
    quickHull(points, points[ind], p2, -findSide(points[ind], p2, p1))
 
def getHull(points):
    # a[i].second -> y-coordinate of the ith point
    n = len(points)
    if (n < 3):
        print("Convex hull not possible")
        return []
        
    # Finding the point with minimum and
    # maximum x-coordinate
    min_x = 0
    max_x = 0
    for i in range(1, n):
        if points[i][0] < points[min_x][0]:
            min_x = i
        if points[i][0] > points[max_x][0]:
            max_x = i
 
    # Recursively find convex hull points on
    # one side of line joining a[min_x] and
    # a[max_x]
    quickHull(points, points[min_x], points[max_x], 1)
 
    # Recursively find convex hull points on
    # other side of line joining a[min_x] and
    # a[max_x]
    quickHull(points, points[min_x], points[max_x], -1)
 
    print("The points in Convex Hull are:")
    print(hull)
    return list(hull)
 
if __name__ == '__main__':
    points = [(1, 3), (3, 3), (3, 5), (4, 5), (5, 2), (6, 3), (6, 6), (8, 4), (9, 1), (10, 2)]
    # points = [(0, 0), (1, 3), (2, 1), (3, 2), (4, 3), (5, 0), (6, 2), (7, 1)]
    # points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
    hull = getHull(points)
    # test = getHull(points)
    
    # visualization
    points = np.array(points)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3))
    
    # Use this to 
    test = ConvexHull(points)
    for ax in (ax1, ax2):
        ax.plot(points[:, 0], points[:, 1], '.', color='k')
        if ax == ax1:
            ax.set_title('Given points')
        else:
            ax.set_title('Convex hull')
            for simplex in test.simplices:
                ax.plot(points[simplex, 0], points[simplex, 1], 'c')
            ax.plot(points[test.vertices, 0], points[test.vertices, 1], 'o', mec='r', color='none', lw=1, markersize=10)
        ax.set_xticks(range(10))
        ax.set_yticks(range(6))
    plt.show()