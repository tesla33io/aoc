import re

def atoi(d_list: list):
    d_list = [int(d) for d in d_list]
    return d_list

def main(file_name: str):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print(len(lines))
            num_sum = 0
            for line in lines:
                digits = re.findall("\d", line)
                digits = atoi(digits)
                num_sum += (digits[0] * 10) + digits[-1]
                print((digits[0] * 10) + digits[-1], end="  > 1\n")
            print(num_sum)
    except Exception as e:
        print(e)
        print("\nError: can\'t open your file.")


if __name__ == "__main__":
    fn = input("Input file: ")
    if not fn:
        fn = "input.txt"
    main(fn)