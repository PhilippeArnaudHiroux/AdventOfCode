file_Name = "Day_3.txt"

def part_1(file_Path):
    count = 0
    with open(file_Path, 'r') as file:
        for line in file:
            input = line.split()
            input = [int(x) for x in input]
            input = sorted(input)
            if input[0] + input[1] > input[2]:
                count += 1
    
    print(count)

def part_2(file_Path):
    count = 0
    first_List = []
    second_List = []
    third_List = []
    with open(file_Path) as file:
        input = file.read()
    
    input = input.split('\n')
    input = [list(map(int, row.split())) for row in input]
    first_List = [element[0] for element in input]
    second_List = [element[1] for element in input]
    third_List = [element[2] for element in input]
    first_List = sorted(first_List)
    second_List = sorted(second_List)
    third_List = sorted(third_List)
    for i in range(0, len(first_List), 3):
        if first_List[i] + first_List[i+1] > first_List[i+2]:
            count += 1
        if second_List[i] + second_List[i+1] > second_List[i+2]:
            count += 1
        if third_List[i] + third_List[i+1] > third_List[i+2]:
            count += 1
    
    print(count)

part_1(file_Name)
part_2(file_Name)