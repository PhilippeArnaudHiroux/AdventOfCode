file_Path = "Day_5.txt"

with open(file_Path, 'r') as file:
    input = [int(line.strip()) for line in file]

def part_1(input_List):
    steps = 0
    current_position = 0

    while 0 <= current_position < len(input_List):
        offset = input_List[current_position]
        input_List[current_position] += 1
        current_position += offset
        steps += 1

    print(steps)

def part_2(input_List):
    steps = 0
    current_position = 0

    while 0 <= current_position < len(input_List):
        offset = input_List[current_position]

        if offset >= 3:
            input_List[current_position] -= 1
        else:
            input_List[current_position] += 1

        current_position += offset
        steps += 1

    print(steps)

part_1(input)
part_2(input)