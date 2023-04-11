#!/usr/bin/env python3

import re
import sys


def file_listing(filename="src/listing.txt"):
    f = open(filename, "r")

    pattern = r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)'

    result = []


    for line in f:
        x = re.search(r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)', line)
        size, month, day, hour, minute, filename = x.groups()
        result.append((int(size), month, int(day), int(hour), int(minute), filename)) 

        print(result)
    
    return(result)





def main():
    file_listing()
    pass

if __name__ == "__main__":
    main()
