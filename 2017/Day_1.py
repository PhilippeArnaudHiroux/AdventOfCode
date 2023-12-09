file_Name = "Day_1.txt"

def part_1(file_Path):
    input = []
    count = 0
    with open(file_Path, 'r') as file:
        for line in file:
            input = list(line)

    input = [int(digit) for digit in input]

    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            count += input[i]

    if input[0] == input[len(input)-1]:
        count += input[0]

    print(count)

def part_2(file_Path):
    input = []
    count = 0
    with open(file_Path, 'r') as file:
        for line in file:
            input = list(line)

    input = [int(digit) for digit in input]
    size = len(input) / 2
    size = int(size)
    
    for i in range(size):
        if input[i] == input[i+size]:
            count += input[i]*2

    print(count)

part_1(file_Name)
part_2(file_Name)