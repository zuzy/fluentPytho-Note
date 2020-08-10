#!/usr/bin/python3
from math import hypot

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        # return 'Vector({}, {})'.format(self.x, self.y)
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)                    
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
def test():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    v = Vector(3, 4)
    print(v, 'abs: {}'.format(abs(v)))
    v *= 3
    print(v, 'abs: {}'.format(abs(v)))
    vv = Vector('1', '2')
    print(vv)

if __name__ == '__main__':
    test()