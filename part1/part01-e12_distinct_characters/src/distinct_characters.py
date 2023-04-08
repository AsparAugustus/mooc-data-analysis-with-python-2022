#!/usr/bin/env python3

def distinct_characters(L):

    newDict = {}
    for word in L:
        unique_chars = len(set(word))
        newDict[word] = unique_chars




    return newDict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
