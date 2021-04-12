# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

from math import sqrt


def find_next_square(sq):
    if sqrt(sq) - int(sqrt(sq)) == 0.0:
        return (sqrt(sq) + 1) ** 2
    else:
        return -1
