from itertools import combinations

def on_same_circumference(points):
    """
    Determines whether all points in the given list lie on the same circumference.
    Returns True if they do, False otherwise.
    """
    n = len(points)
    
    # Check if there are at least three points
    if n < 3:
        return True
    
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    # Calculate center (a,b) and radius r of circle
    # These formulas are derived from the equation of a circle:
    # (x - a)^2 + (y - b)^2 = r^2
    # where (a,b) is the center of the circle and r is its radius. By plugging in the coordinates 
    # of the three given points into this equation, we get three equations with three unknowns (a, b, and r). 
    # We can then solve for a, b, and r using standard algebraic techniques to obtain the formulas above.
    a = (x1**2 + y1**2)*(y2 - y3) + (x2**2 + y2**2)*(y3 - y1) + (x3**2 + y3**2)*(y1 - y2)
    b = (x1**2 + y1**2)*(x3 - x2) + (x2**2 + y2**2)*(x1 - x3) + (x3**2 + y3**2)*(x2 - x1)
    c = 2*((x1*(y2 - y3)) + (x2*(y3 - y1)) + (x3*(y1 - y2)))
    center = (a/c, b/c)
    radius = ((x1 - center[0])**2 + (y1 - center[1])**2)**0.5
    
    
    # Check if all points lie on any of the circles
    for point in points:
        if ((point[0] - center[0])**2 + (point[1] - center[1])**2)**0.5 != radius:
            return False
        
    return True

points = [(1, -1), (-1, 1), (1, 1), (-1, -1)]
print(on_same_circumference(points))  # Returns True
