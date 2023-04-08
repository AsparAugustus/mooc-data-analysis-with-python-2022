import math

# Enter you module contents here

__version__ = '1.0'
__author__ = 'AsparAugustus'

def hypotenuse(side1, side2):
    """
    Calculate the length of the hypotenuse of a right-angled triangle.

    Args:
        side1 (float): The length of one of the other sides.
        side2 (float): The length of the other other side.

    Returns:
        float: The length of the hypotenuse.
    """
    c = math.sqrt(side1 ** 2 + side2**2)
    return c

def area(base, height):
    """
    Calculate the area of a right-angled triangle.

    Args:
    base (float): The length of the base.
    height (float): The length of the height.

    Returns:
    float: The area of the triangle.
    """
    area = (base*height)/2
    return area