import re

file_path = 'Day_1.txt'
with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

def part_1(lines_array):
    lines_array = [re.sub('[a-zA-Z]', '', string) for string in lines_array]
    first_digit = [next((char for char in element if char.isdigit()), None) for element in lines_array]
    last_digit = [next((char for char in reversed(element) if char.isdigit()), None) for element in lines_array]

    combined_array = list(zip(first_digit, last_digit))
    concatenated_array = [''.join(pair) for pair in combined_array]
    integer_array = [int(element) for element in concatenated_array]

    result = sum(integer_array)

    print(result)

def part_2(lines_array):
    lines_array = [s.replace("one", "on1e") for s in lines_array]
    lines_array = [s.replace("two", "t2wo") for s in lines_array]
    lines_array = [s.replace("three", "t3hree") for s in lines_array]
    lines_array = [s.replace("four", "fo4ur") for s in lines_array]
    lines_array = [s.replace("five", "fi5ve") for s in lines_array]
    lines_array = [s.replace("six", "s6ix") for s in lines_array]
    lines_array = [s.replace("seven", "se7ven") for s in lines_array]
    lines_array = [s.replace("eight", "e8ight") for s in lines_array]
    lines_array = [s.replace("nine", "ni9ne") for s in lines_array]

    lines_array = [re.sub('[a-zA-Z]', '', string) for string in lines_array]

    first_digit = [next((char for char in element if char.isdigit()), None) for element in lines_array]
    last_digit = [next((char for char in reversed(element) if char.isdigit()), None) for element in lines_array]

    combined_array = list(zip(first_digit, last_digit))
    concatenated_array = [''.join(pair) for pair in combined_array]
    integer_array = [int(element) for element in concatenated_array]

    result = sum(integer_array)
    print(result)

part_1(input)
part_2(input)