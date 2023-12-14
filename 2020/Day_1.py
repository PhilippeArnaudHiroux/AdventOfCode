file_Name = "Day_1.txt"

def part_1(file_Path):
    with open(file_Path, 'r') as file:
        input = [int(line.strip()) for line in file]

    value_1 = 0
    value_2 = 0
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] + input[j] == 2020:
                value_1 = input[i]
                value_2 = input[j]

    print(value_1 * value_2)

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [int(line.strip()) for line in file]

    value_1 = 0
    value_2 = 0
    value_3 = 0
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            for k in range(j + 1, len(input)):
                if input[i] + input[j] + input[k] == 2020:
                    value_1 = input[i]
                    value_2 = input[j]
                    value_3 = input[k]

    print(value_1 * value_2 * value_3)

part_1(file_Name)
part_2(file_Name)
