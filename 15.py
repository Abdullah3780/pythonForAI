# Write a function which take the radius of circle as first argument and a char (a or c) as second argument. If second
# argument is a then return the area of circle. If the second argument is c then return the circumference of circle
from cmath import pi


def area_circum(radius, sym):
    if(sym == 'a'):
        return pi*radius**2
    elif(sym == 'c'):
        return 2*pi*radius


print(str(area_circum(radius=2, sym='a')))
