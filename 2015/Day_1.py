file_path = 'Day_1.txt'
with open(file_path, 'r') as file:
    input = file.read()

def part_1(input_List):
    result = 0

    for i in range(len(input_List)):
        if input[i] == '(':
            result += 1
        else:
            result += -1

    print(result)

def part_2(input_List):
    result = 0
    for i in range(len(input_List)):
        if input[i] == '(':
            result += 1
        else:
            result += -1

        if result < 0:
            print(i)
            break
        
part_1(input)
part_2(input)

