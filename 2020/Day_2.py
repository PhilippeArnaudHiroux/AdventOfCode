file_Name = "Day_2.txt"

def part_1(file_Path):
    min_Number = 0
    max_Number = 0
    char = ""
    string = ""
    result = 0

    with open(file_Path, 'r') as file:
        for line in file:
            input = line.split(":")
            string = input[1]
            string = string.replace(" ", "")
            input = input[0].split(" ")
            char = input[1]
            min_Number, max_Number = input[0].split("-")
            min_Number = int(min_Number)
            max_Number = int(max_Number)

            count = string.count(char)
            if count >= min_Number and count <= max_Number:
                result += 1
    
    print(result)

def part_2(file_Path):
    position_1 = 0
    position_2 = 0
    char = ""
    string = ""
    result = 0

    with open(file_Path, 'r') as file:
        for line in file:
            input = line.split(":")
            string = input[1]
            string = string.replace(" ", "")
            input = input[0].split(" ")
            char = input[1]
            position_1, position_2 = input[0].split("-")
            position_1 = int(position_1)
            position_2 = int(position_2)

            if string[position_1-1] == char and string[position_2-1] != char or string[position_1-1] != char and string[position_2-1] == char:
                result += 1

    print(result)

#part_1(file_Name)
part_2(file_Name)