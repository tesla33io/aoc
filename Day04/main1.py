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


def total_cards(matching: dict) -> list:
    total = {}
    for k in matching:
        total[k] = 1
    for k, v in matching.items():
        print(f"\tk: {k} v: {v}")
        for i in range(len(v)):
            print(f"\t\tk + 1 + i: {k + 1 + i}")
            total[k + i] += 1
    print("+"*10)
    print(total)
    print("+"*10)
    return sorted(total)


def main(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        l = 0
        p_sum = 0
        m_dict = {}
        for line in lines:
            l += 1
            winning  = get_winning_numbers(line)
            my       = get_my_numbers(line)
            matching = get_matching(winning, my)
            points   = count_points(matching)
            p_sum += points
            m_dict[l] = matching
            print(f"{l}. ({points}) {matching}")
        print(f"\nPoints sum: {p_sum}\n\nPart two:")
        total = total_cards(m_dict)
        total_dict = {i:total.count(i) for i in total}
        total_cards_count = 0 
        for i in total_dict:
            total_cards_count += total_dict[i]
        print(total)
        print(total_dict)
        print(total_cards_count)


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