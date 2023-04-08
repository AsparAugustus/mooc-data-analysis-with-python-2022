#!/usr/bin/env python3


def main():
    for number in range(11):
        if number != 0: 

            for number2 in range (11):
                if number2 !=0:
                    if number2 != 10:
                        print('{:2d}'.format(number * number2), end="  ")
                    else:
                        print('{:2d}'.format(number * number2), end="\n")



if __name__ == "__main__":
    main()
