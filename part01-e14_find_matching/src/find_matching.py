#!/usr/bin/env python3

def find_matching(L, pattern):

    index_found = []

    for index, word in enumerate(L):
        if pattern in word:
            index_found.append(index)


    print(index_found)

    return index_found

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    pass

if __name__ == "__main__":
    main()
