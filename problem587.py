import math
from itertools import count

# the diagonal equation for d circles
def diag(d, x):
    return 1 / d * x + (1 - 1 / d)

# intersect the diagonal with the last circle's arc 0..pi/2
# for d circles. solved to x using wolfram alpha
def intersect(d):
    x = (1 - d) / (d**2 + 1) + 2**0.5 * (d**3 / (d**2 + 1)**2)**0.5
    return x

# integrate the circle arc from 0 .. the intersection. using wolfram alpha
def area_arc(x):
    return 1 / 2 * ((1 - x ** 2) ** 0.5 * x + math.asin(x))

# compute the left-over triangle not included in the integral
def area_small_triangle(d, xi):
    a = (1-xi)
    b = (1-diag(d, xi))
    return a*b/2

# compute the area of the concave triangle for d triangles by subtracting the
# circle arc area from its bounding box, which yields the concave part
def area_concave_triangle(d):
    xi = intersect(d)
    small_triangle = area_small_triangle(d, xi)
    arc = area_arc(xi)
    return (1*xi - arc) + small_triangle

r_circles = 1
area_circle = math.pi
area_l_section = (2 * 2 - area_circle) / 4

for d in count(2):
    if area_concave_triangle(d) / area_l_section < 0.001:
        print ("value of n is", d)
        break
