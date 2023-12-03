import os


def string_to_dict(input_string):
    game_dict = {}
    games = input_string.split(';')
    game_info = input_string.split(':')
    game_number = game_info[0].strip()
    sets_of_colors = game_info[1].strip().split(';')

    game_dict[game_number] = []

    for set_colors in sets_of_colors:
        colors = set_colors.strip().split(', ')
        color_dict = {}
        for color in colors:
            quantity, col = color.split(' ')
            color_dict[col] = int(quantity)
        game_dict[game_number].append(color_dict)
    return (game_dict)


def main(file_name):
    with open(file_name, 'r') as file:
        num_sum = 0
        lines = file.readlines()
        for line in lines:
            red_max = 0
            green_max = 0
            blue_max = 0
            data = string_to_dict(line)
            game = line.split(": ")[0]
            for s in data[game]:
                if "red" in s:
                    if s["red"] > red_max:
                        red_max = s["red"]
                if "green" in s:
                    if s["green"] > green_max:
                        green_max = s["green"]
                if "blue" in s:
                    if s["blue"] > blue_max:
                        blue_max = s["blue"]
            print(f"{game} : red {red_max}, green {green_max}, "
                f"blue {blue_max}")
            power = red_max * green_max * blue_max
            num_sum += power
        print("Sum: " + str(num_sum))


if __name__ == "__main__":
    fn = input("Input file: ")
    if not fn:
        fn = "input.txt"
    if os.path.exists(fn):
        main(fn)
    else:
        print("Error: file dose not exists.")