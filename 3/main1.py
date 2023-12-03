import os
import sys


def get_sym_pos(lines: list) -> list:
    syms = []
    for h in range(len(lines)):
        lines[h] = lines[h].replace("\n", "")
        for w in range(len(lines[h])):
            if (lines[h][w] != '.' and not lines[h][w].isdigit()):
                syms.append({'c': lines[h][w], 'h': h, 'w': w})
    return syms


def get_num_pos(lines: list) -> list:
    nums = []
    for h in range(len(lines)):
        w = 0
        while w < len(lines[h]):
            if lines[h][w].isdigit():
                s_w = w
                while w < len(lines[h]) and lines[h][w].isdigit():
                    w += 1
                e_w = w
                nums.append({'h': h, 'sw': s_w, 'ew': e_w})
            else:
                w += 1
    return nums


def check_pos(syms: list, nums: list) -> list:
    checked = []
    for num in nums:
        for sym in syms:
            if ((num['h'] == sym['h']) or
                (num['h'] == (sym['h'] - 1)) or
                (num['h'] == (sym['h'] + 1))):
                if (sym['w'] >= (num['sw'] - 1) and sym['w'] <= num['ew']):
                    checked.append(num)
    return (checked)


def get_gear_nums(syms: list, nums: list) -> list:
    gears = {}
    for sym in syms:
        if sym['c'] == '*':
            k = f"{sym['c']}w{sym['w']}h{sym['h']}"
            gears[k] = []
            for num in nums:
                if ((num['h'] == sym['h']) or
                    (num['h'] == (sym['h'] - 1)) or
                    (num['h'] == (sym['h'] + 1))):
                    if (sym['w'] >= (num['sw'] - 1) and sym['w'] <= num['ew']):
                        gears[k].append(num)
    return gears


def get_gear_ratios(gears: list, lines: list) -> list:
    ratios = []
    for gear in gears:
        ratio = []
        for num in gears[gear]:
            ratio.append(int(lines[num['h']][int(num['sw']):int(num['ew'])]))
        if (len(ratio) == 2):
            ratios.append(ratio)
    return ratios


def main(file_name: str) -> None:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        symbol_pos = get_sym_pos(lines)
        num_pos = get_num_pos(lines)
        checked = check_pos(symbol_pos, num_pos)
        num_sum = 0
        for i in checked:
            num_sum += int(lines[i['h']][i['sw']:i['ew']])
        print(f"Sum: {num_sum}")
        gears_data = get_gear_nums(symbol_pos, num_pos)
        ratios = get_gear_ratios(gears_data, lines)
        ratio_sum = 0
        for ratio in ratios:
            ratio_sum += (ratio[0] * ratio[1])
        print(f"Ratio sum: {ratio_sum}")


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
        print("Error: file dose not exists.")