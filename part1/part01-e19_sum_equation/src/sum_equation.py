#!/usr/bin/env python3



def sum_equation(L):

    sum = 0
    sum_text = ""

    if len(L) == 0:
    
        return "0 = 0"


    for i, number in enumerate(L):

        if i != len(L):

            sum = sum + number
            print(type(number))


            num = str(number)
            sum_text += num + " + "

        #remove the last plus sign

        equation = sum_text[:-3]
        solution_text = " = " + str(sum)
        equation += solution_text


    return equation

        

def main():
    pass

if __name__ == "__main__":
    main()
