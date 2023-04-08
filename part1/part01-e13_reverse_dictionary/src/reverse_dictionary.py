#!/usr/bin/env python3

def reverse_dictionary(d):

    #fetch dict
    #put all values into a list from dict
    #for each value, make a new key

    reversed_dict = {}
    for key, value in d.items():
        temp_list = []
        for word in value:
            temp_list.extend(word)

            #check if key already exists
            if word not in reversed_dict:
                reversed_dict[word] = [key]
            else:
                reversed_dict[word].append(key)
            
        
    print(reversed_dict)


    return reversed_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)
    pass

if __name__ == "__main__":
    main()
