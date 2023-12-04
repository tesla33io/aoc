import os
import sys


def get_winning_numbers(string: str) -> list:
    string = string.split(": ")[1].split(" | ")[0]
    return [int(number) for number in string.split()]


def get_my_numbers(string: str) -> list:
    string = string.split(": ")[1].split(" | ")[1]
    return [int(number) for number in string.split()]


def get_matching(winning: list, my: list) -> list:
    matching = []
    for num in winning:
        for n in my:
            if (num == n):
                matching.append(n)
    return matching


def count_points(matching: list) -> list:
    if len(matching) < 1:
        return 0
    count = 1
    for i in range(len(matching) - 1):
        count *= 2
    return count


def main(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        l = 0
        p_sum = 0
        for line in lines:
            l += 1
            winning  = get_winning_numbers(line)
            my       = get_my_numbers(line)
            matching = get_matching(winning, my)
            points   = count_points(matching)
            p_sum += points
            print(f"{l}. ({points}) {matching}")
        print(f"\nPoints sum: {p_sum}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        fn = sys.argv[1]
    else:
        fn = input("File name: ")
    if not fn:
        fn = "input.txt"
    if os.path.exists(fn):
        main(fn)
    else:
        print("\nError: file dose not exists.\n")