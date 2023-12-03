import re
import os
import traceback

s_digits = {
    "one"	:	"1",
    "two"	:	"2",
    "three"	:	"3",
    "four"	:	"4",
    "five"	:	"5",
    "six"	:	"6",
    "seven"	:	"7",
    "eight"	:	"8",
    "nine"	:	"9",
}

def check_in(elements: list, string: str):
    for element in elements:
        if element in string:
            return element

def con_first(string: str):
    for i in range(len(string)):
        el = check_in(s_digits, string[0:i])
        if el:
            return (int(s_digits[el]))
        if string[i].isdigit():
            return (int(string[i]))


def con_last(string: str):
    for i in range(len(string) - 1, -1, -1):
        el = check_in(s_digits, string[i:])
        if el:
            return (int(s_digits[el]))
        if string[i - 1].isdigit():
            return (int(string[i - 1]))


def convert_s_digit(string: str):
    for k, v in s_digits.items():
        string = string.replace(k, v)
    return string

def main(file_name: str):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(len(lines))
        num_sum = 0
        l = 0
        for line in lines:
            l += 1
            fd = con_first(line)
            ld = con_last(line)
            num_sum += fd * 10 + ld
            print(f"{l}. {fd} - {ld}")
        print("Sum: " + str(num_sum))


if __name__ == "__main__":
    fn = input("Input file: ")
    if not fn:
        fn = "input.txt"
    if os.path.exists(fn):
        main(fn)
    else:
        print("Error: file dose not exists.")