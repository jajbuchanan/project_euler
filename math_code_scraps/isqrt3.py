# Python Program to explain
# math.isqrt() method

import math

n = 11


def Next(n):
    # Get the ceiling of
    # the exact square root of n:
    ceil = 1 + math.isqrt(n)

    # print the next perfect square of n

    print("Next perfect square after {} is {}".format(n, ceil * ceil))


# Driver's code
Next(11)
Next(37)
