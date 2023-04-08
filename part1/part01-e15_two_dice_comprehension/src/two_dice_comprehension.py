#!/usr/bin/env python3

def main():

    # dice_list = []
    # for dice_num in range(1, 6):
    #     for dice_num2 in range(1, 6):
    #         total = dice_num + dice_num2
    #         if total == 5:
    #             # print(f"({dice_num}, {dice_num2})")
    #             dice_list.append(f'({dice_num}), ({dice_num2})')


    s = [print((x, y)) for x in range(1, 7) for y in range(1, 7) if x + y == 5]


    

if __name__ == "__main__":
    main()
