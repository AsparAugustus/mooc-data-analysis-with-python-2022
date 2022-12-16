#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):

    x = (-b + math.sqrt(b*b - 4 * a * c))/ (2 * a)

    x2 = x = (-b - math.sqrt(b*b - 4 * a * c))/ (2 * a)

    return (x, x2)


def main():
    pass




    

if __name__ == "__main__":
    main()
