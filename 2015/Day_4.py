import hashlib

file_path = 'Day_4.txt'
with open(file_path, 'r') as file:
    input = file.read()

def part_1(input_List):
    number = 1
    while True:
        input_str = input_List + str(number)
        hash = hashlib.md5(input_str.encode()).hexdigest()
        if hash.startswith('00000'):
            print(number)
            break

        number += 1

def part_2(input_List):
    number = 1
    while True:
        combined_str = input_List + str(number)
        hash = hashlib.md5(combined_str.encode()).hexdigest()
        if hash.startswith('000000'):
            print(number)
            break

        number += 1

part_1(input)
part_2(input)