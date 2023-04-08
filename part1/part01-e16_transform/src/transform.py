#!/usr/bin/env python3

def transform(*args):

    newList = []
    for arg in args:
        arg = arg.split()
        newList.append(arg)
        



    zipped = zip(*newList)

  

    s = list(map(lambda x : int(x[0]) * int(x[1]), zipped))

    print(s)



    return s

def main():
    transform("1 5 3", "2 6 -1") 

    pass

if __name__ == "__main__":
    main()
