#!/usr/bin/env python3

def _sort(list):

    original_list = list.copy()
    lowest = min(original_list)
    newList = []

    def internal_sort(list):


        for index, num in enumerate(original_list):

            if num <= lowest:
                lowest = num
                newList.append(lowest)
                original_list.pop(index)

                print(original_list)

     
        







def merge(L1, L2):

    new_list = L1 + L2
    _sort(new_list)

    return new_list

def main():

    merge([1, 2 ,3], [5, 7, 6])

    pass

if __name__ == "__main__":
    main()
