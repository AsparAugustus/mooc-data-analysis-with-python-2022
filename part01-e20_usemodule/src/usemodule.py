#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here

    # Call the hypotenuse function
    side1 = 3
    side2 = 4
    hypotenuse_length = triangle.hypotenuse(side1, side2)
    print(f'The hypotenuse length is {hypotenuse_length:.2f}')

    # Call the area function
    base = 5
    height = 10
    area = triangle.area(base, height)
    print(f'The area of the triangle is {area:.2f}')


if __name__ == "__main__":
    main()
