# Lab test 2: Write a Python class t present a 2D vector
# 6/12/18
# Louis Chavez

import math


class Vector(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__magnitude = math.sqrt((self.__x ** 2) + (self.__y ** 2))
    # end init

    def set_newx(self, newx):
        self.__x = newx
    # end setx

    def set_newy(self, newy):
        self.__y = newy
    # end setx

    def get_x(self):
        return self.__x
    # end get_x

    def get_y(self):
        return self.__y
    # end get_y

    def __add__(self, v2):
        new_x = self.__x + v2.get_x()
        new_y = self.__y + v2.get_y()
        return Vector(new_x, new_y)
    # end add

    def __mul__(self, v2):
        if type(v2) is int:
            self.__x = self.__x * v2
            self.__y = self.__y * v2
            self.__magnitude = math.sqrt((self.__x ** 2) + (self.__y ** 2))
        else:
            scalar = (self.__x * v2.get_x()) + (self.__y * v2.get_y())
            return scalar
        # end if
    # end muls

    def __sub__(self, v2):
        new_x = self.__x + (v2.get_x() * -1)
        new_y = self.__y + (v2.get_y() * -1)
        return Vector(new_x, new_y)
    # end sub

    def magnitude(self):
        print("The magnitude of vector is:", self.__magnitude)
    # end magnitude

    def __str__(self):
        return "({},{})".format(self.__x, self.__y)
    # end str
# end class Vector


def main():
    v1 = Vector(1, 2)
    print("Printing v1")
    print(v1)

    v2 = Vector(2, 2)
    print("\nPrinting v2")
    print(v2)

    print("\nAdding v1 and v2")
    v3 = v1 + v2
    print("printing v3")
    print(v3)

    print("\nSubtracting v2 and v1")
    v4 = v2 - v1
    print("Printing v4")
    print(v4)

    print("\nMultiplying v1 and v2")
    print("Resulting scalar:", v1 * v2)

    print("\nMultiplying v1 with an integer")
    v1 * 3
    print(v1)

    print("\nCalculating magnitude of v3")
    v3.magnitude()
# end main


main()