file_Name = "Day_2.txt"

def part_1(file_Path):
    input = []
    result = 0
    max_Value = 0
    min_Value = 0

    with open(file_Path, 'r') as file:
        input = [line.split("\t") for line in file]

    input = [[element.rstrip('\n') for element in sublist] for sublist in input]
    input = [[int(element) for element in sublist] for sublist in input]

    for i in range(len(input)):
        max_Value = max(input[i])
        min_Value = min(input[i])
        result += max_Value - min_Value

    print(result)


part_1(file_Name)