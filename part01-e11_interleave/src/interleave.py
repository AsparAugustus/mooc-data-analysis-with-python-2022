#!/usr/bin/env python3

def interleave(*lists):
    # length_of_list = len(lists)
    # newlist = []


    


    # def appendArray(array_index):
    #     for list in lists:
    #         # newlist.append(list[start])
    #         newlist.append(list[array_index])
    


    # for loop in range(length_of_list):
    #    appendArray(loop)

    newList = []
    zipped = zip(*lists)
    
    for item in zipped:
        newList.extend(item)

    # for x, y, z in zipped:
    #     print(x, y, z)
    
    # print(newList)

    return newList






def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
