#!/usr/bin/env python3

def area(height, base):
    '''(number, number) -> number

    Return the area of the triangle with height x base / 2.

    >>> area(3,4)
    6
    >>> area(7,4)
    14
    '''
    return (height * base) / 2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the perimeter of the triangle with sides of
    length side1, side2 and side3.

    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''

    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the semiperimeter of the triangle with side of
    lenght side1, side2 and side3.

    >>> semiperimeter(3, 4, 5)
    6
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''

    return perimeter(side1, side2, side3) / 2

