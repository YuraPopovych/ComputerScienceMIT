def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        if a % b == 0:
            return b
        else:
            return gcdRecur(a, a % b)
    else:
        if b % a == 0:
            return a
        else:
            return gcdRecur(b, b % a)


print(gcdRecur(2, 12))

print(gcdRecur(6, 12))

print(gcdRecur(9, 12))

print(gcdRecur(17, 12))