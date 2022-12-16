#!/usr/bin/env python3

def triple (num):
    return num*3


def square (num):
    return num*num


def main():


    for num in range(1, 10):
        tripled = triple(num)
        squared = square(num)

        if(squared > tripled):
            break

        print(f'triple({num})=={tripled} square({num})=={squared}')


if __name__ == "__main__":
    main()
