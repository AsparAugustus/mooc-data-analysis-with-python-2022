#!/usr/bin/env python3

import re



def red_green_blue(filename="src/rgb.txt"):

    with open(filename, 'r') as f:

        #skip first line
        next(f)

        result_list = []

        for i, line in enumerate(f):


            #clean up whitespaces, first starting with any 1 or more consecutive white spaces
            double_whitespace_pattern = r"\s{2,}"
            text = re.sub(double_whitespace_pattern, ' ', line)
            

            


            # #delete whitespace between words for colour
            # digit_whitespace_pattern = r"([a-zA-Z])\s+([a-zA-Z])"
            # text = re.sub(digit_whitespace_pattern, r'\1\2', text)

         

            #find each line by pattern
            pattern = r"\b\d+\s+\d+\s+\d+\s+.+\b"
            text = re.findall(pattern, text)
            

            #turning the list output of findall into string
            result = "".join(text)

            #substitute whitespaces between entry with \t
            result = re.sub(r"(\d+)\s(\d+)\s(\d+)\s", r"\1\t\2\t\3\t", result)

            result_list.append(result)

            print(repr(result))



    return result_list


def main():
    red_green_blue()
    pass

if __name__ == "__main__":
    main()
