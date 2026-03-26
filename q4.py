# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math as m 

def circleStats(r):
    area = m.pi * (r**2)
    circum = 2*(m.pi * r)
    return area , circum

a,b = circleStats(32)
print(f"area of circle is : {a:.2f}")
print(f"circumference of circle is : {b:.2f}")