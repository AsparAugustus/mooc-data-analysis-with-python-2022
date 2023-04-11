#!/usr/bin/env python3
import re


def integers_in_brackets(text):

    text = re.sub(r"\s+", "", text)
    print(text)



    # pattern = r"\[\s*[\+\-]\d+\s*]"
    pattern = r"\[[\+\-]?\d+]"
    matches = re.findall(pattern, text)

    removed_brackets_list = []

    for word in matches:
        removed_brackets = re.sub(r"[\[\]]", "", word)
        
        removed_brackets_list.append(int(removed_brackets))

    

    print(removed_brackets_list)
    return removed_brackets_list

def main():
    integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")
    pass

if __name__ == "__main__":
    main()
