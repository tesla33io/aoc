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
        red_max = 12
        green_max = 13
        blue_max = 14
        num_sum = 0
        lines = file.readlines()
        for line in lines:
            data = string_to_dict(line)
            game = line.split(": ")[0]
            ok = True
            for s in data[game]:
                if (("red" in s and s["red"] > red_max) or
                    ("green" in s and s["green"] > green_max) or
                    ("blue" in s and s["blue"] > blue_max)):
                    ok = False
            if ok:
                num_sum += int(game.split(" ")[1])
        print("Sum: " + str(num_sum))


if __name__ == "__main__":
    fn = input("Input file: ")
    if not fn:
        fn = "input.txt"
    if os.path.exists(fn):
        main(fn)
    else:
        print("Error: file dose not exists.")