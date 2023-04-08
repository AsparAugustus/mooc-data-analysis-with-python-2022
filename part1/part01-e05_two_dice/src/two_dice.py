#!/usr/bin/env python3

def main():
    for dice_num in range(1, 6):
        for dice_num2 in range(1, 6):
            total = dice_num + dice_num2
            if total == 5:
                print(f"({dice_num}, {dice_num2})")

if __name__ == "__main__":
    main()


