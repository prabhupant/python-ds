# Reference - https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/

import math

def egyptian_fraction(nr, dr):
    ef = []

    while nr != 0:
        x = math.ceil(dr / nr)
        ef.append(x)

        nr = x * nr - dr
        dr = dr * x
