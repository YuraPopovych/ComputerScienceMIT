def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    greatest_divisor = None
    
    if a > b:
        range_limit = a
    else:
        range_limit = b
        
    for divisior in range(1, range_limit + 1):
        if a % divisior == 0 and b % divisior == 0:
            greatest_divisor = divisior
    return greatest_divisor

print(gcdIter(2, 12))

print(gcdIter(6, 12))

print(gcdIter(9, 12))

print(gcdIter(17, 12))