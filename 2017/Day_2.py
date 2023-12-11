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

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.split("\t") for line in file]

    input = [[element.rstrip('\n') for element in sublist] for sublist in input]
    input = [[int(element) for element in sublist] for sublist in input]
    
    result = 0

    for sublist in input:
        length_Sublist = len(sublist)
        for i in range(length_Sublist):
            for j in range(i + 1, length_Sublist):
                if sublist[i] % sublist[j] == 0 or sublist[j] % sublist[i] == 0:
                    if sublist[i] > sublist[j]:
                        result += sublist[i] / sublist[j]
                    else:
                        result += sublist[j] / sublist[i]
    
    print(result)

part_1(file_Name)
part_2(file_Name)

