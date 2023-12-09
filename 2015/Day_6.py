import numpy as np

file_Name = "Day_6.txt"

def part_1(file_Path):
    size = 1000
    light = np.zeros((size, size), dtype=int)

    instruction = ""
    fist_Coordinate = ""
    second_Coordinate = ""
    start_X = 0
    end_X = 0
    start_Y = 0
    end_Y = 0

    with open(file_Path, 'r') as file:
        for line in file:
            if "turn on" in line:
                instruction = "turn on"
                line = line.replace("turn on ", "")
            if "turn off" in line:
                instruction = "turn off"
                line = line.replace("turn off ", "")
            if "toggle" in line:
                instruction = "toggle"
                line = line.replace("toggle ", "")

            line = line.replace("through ", "")
            fist_Coordinate, second_Coordinate = line.split(" ")
            start_X, start_Y = fist_Coordinate.split(",")
            end_X, end_Y = second_Coordinate.split(",")
            start_X = int(start_X)
            start_Y = int(start_Y)
            end_X = int(end_X)
            end_Y = int(end_Y)

            if instruction == "turn on":
                for i in range(start_Y, end_Y+1, 1):
                    for j in range(start_X, end_X+1, 1):
                        light[i][j] = 1

            if instruction == "turn off":
                for i in range(start_Y, end_Y+1, 1):
                    for j in range(start_X, end_X+1, 1):
                        light[i][j] = 0

            if instruction == "toggle":
                for i in range(start_Y, end_Y+1, 1):
                    for j in range(start_X, end_X+1, 1):
                        if light[i][j] == 0:
                            light[i][j] = 1
                        else:
                            light[i][j] = 0
    count = np.count_nonzero(light == 1)
    print(count)

def part_2(file_Path):
    size = 1000
    light = np.zeros((size, size), dtype=int)

    instruction = ""
    fist_Coordinate = ""
    second_Coordinate = ""
    start_X = 0
    end_X = 0
    start_Y = 0
    end_Y = 0

    with open(file_Path, 'r') as file:
        for line in file:
            if "turn on" in line:
                instruction = "turn on"
                line = line.replace("turn on ", "")
            if "turn off" in line:
                instruction = "turn off"
                line = line.replace("turn off ", "")
            if "toggle" in line:
                instruction = "toggle"
                line = line.replace("toggle ", "")

            line = line.replace("through ", "")
            fist_Coordinate, second_Coordinate = line.split(" ")
            start_X, start_Y = fist_Coordinate.split(",")
            end_X, end_Y = second_Coordinate.split(",")
            start_X = int(start_X)
            start_Y = int(start_Y)
            end_X = int(end_X)
            end_Y = int(end_Y)

            if instruction == "turn on":
                for i in range(start_Y, end_Y+1, 1):
                    for j in range(start_X, end_X+1, 1):
                        light[i][j] += 1

            if instruction == "turn off":
                for i in range(start_Y, end_Y+1, 1):
                    for j in range(start_X, end_X+1, 1):
                        light[i][j] -= 1

            if instruction == "toggle":
                for i in range(start_Y, end_Y+1, 1):
                    for j in range(start_X, end_X+1, 1):
                        light[i][j] += 2
    count = 0

    
    print(light)
part_1(file_Name)
part_2(file_Name)