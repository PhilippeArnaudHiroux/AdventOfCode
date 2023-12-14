file_Name = "Day_6.txt"

def part_1(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
    columns = list(zip(*input))
    char = [max(set(column), key=column.count) for column in columns]
    print(''.join(char))

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
    columns = list(zip(*input))
    char = [min(set(column), key=column.count) for column in columns]
    print(''.join(char))


part_1(file_Name)
part_2(file_Name)