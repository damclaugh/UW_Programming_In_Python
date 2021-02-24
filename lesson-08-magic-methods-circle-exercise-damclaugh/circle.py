
#!/usr/bin/env python

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @classmethod
    def from_diameter(cls, diameter):
        radius = cls(diameter/2)
        return radius

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)
            
    def __add__(self, other):
        return self.radius + other.radius
    
    def __mul__(self, number):
        return self.radius * number

    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def sort_key(self):
        return self.radius

        

# STEP 1
c = Circle(4)
print(c.radius)

# STEP 2
print(c.diameter)

# STEP 3
c.diameter = 2
print(c.diameter)
print(c.radius)

# STEP 4
c = Circle(2)
print(c.area)

# STEP 5
c = Circle.from_diameter(8)
print(c.diameter)
print(c.radius)

# STEP 6
c = Circle(4)
print(c)
print(repr(c))
d = eval(repr(c))
print(d.radius)
print(d)

# STEP 7
c1 = Circle(2)
c2 = Circle(4)
print(c1 + c2)
print(c2 * 3)

# STEP 8
print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
c3 = Circle(4)
print(c2 == c3)

circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
circles_sorted = sorted(circles, key=Circle.sort_key)
print(circles_sorted)