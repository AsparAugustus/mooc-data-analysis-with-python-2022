#!/usr/bin/env python3

import math



def area(num):
    print(f'The area is {num}')

def prompt():
    shape = input("Choose a shape (triangle, rectangle, circle) : ")
    return shape



def main():

    while(1):
        shape = prompt()

        if shape == "":
            break
            

        if shape != "triangle" and shape !=  "rectangle" and shape != "circle":
            print("Unknown shape!")
        
 
 

        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))

            _area = base * height / 2
            area(_area)

        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            _area = width * height
            area(_area)

        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            _area = math.pi * radius * radius
            area(_area)





if __name__ == "__main__":
    main()
