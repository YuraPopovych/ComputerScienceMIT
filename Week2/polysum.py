from math import tan, pi

def polysum(n, s):
    """
    :param n : numbers of sides int 
    :param s: side length int
    :return polysum: rounded to 4 decimal places float
    """
    polygon_area =  ( 0.25 * n * (s**2) ) / ( tan(pi / n ) )
    polygon_perimeter = n * s
    result = polygon_area + polygon_perimeter ** 2
    return round(result, 4)


print( polysum(46, 46) )