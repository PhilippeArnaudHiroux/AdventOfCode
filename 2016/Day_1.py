file_Name = "Day_1.txt"

def part_1(file_Path):
    with open(file_Path, 'r') as file:
        input = file.read()

    input = input.replace(" ","")
    input = list(input.split(','))

    x_As = 0
    y_As = 0
    direction = "North"
    print(input)

    for i in range(len(input)):
        left_Right = input[i][:1]
        steps = input[i][1:]
        steps = int(steps)
        print("i", i)
        print(left_Right, steps)

        if direction == "North":
            if left_Right == "L":
                x_As -= steps
                direction = "West"
            else:
                x_As += steps
                direction = "East"
        elif direction == "East":
            if left_Right == "L":
                y_As += steps
                direction = "North"
            else:
                y_As -= steps
                direction = "South"
        elif direction == "South":
            if left_Right == "L":
                x_As += steps
                direction = "East"
            else:
                x_As -= steps
                direction = "West"
        elif direction == "West":
            if direction == "L":
                y_As -= steps
                direction = "South"
            else:
                y_As += steps
                direction = "North"
        
    print(x_As, y_As)
    print(abs(x_As) + abs(y_As))

part_1(file_Name)