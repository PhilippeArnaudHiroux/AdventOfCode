file_path = 'Day_3.txt'
with open(file_path, 'r') as file:
    input = file.read()

def part_1(input_List):
    x_as = 0
    y_as = 0

    location = []
    position = [x_as, y_as]
    location.append(position)

    for i in range(len(input_List)):
        if input_List[i] == "^":
            y_as += 1
        elif input_List[i] == ">":
            x_as += 1
        elif input_List[i] == "v":
            y_as -= 1
        else:
            x_as -= 1

        position = [x_as, y_as]
        location.append(position)

    amount = set(map(tuple, location))
    amount = len(amount)
    print(amount)

def part_2(input_List):
    santa_x_as = 0
    santa_y_as = 0
    santa_Location = []
    santa_Position = [santa_x_as, santa_y_as]
    santa_Location.append(santa_Position)

    robot_x_as = 0
    robot_y_as = 0
    robot_Location = []
    robot_Position = [robot_x_as, robot_y_as]
    robot_Location.append(robot_Position)

    for i in range(0, len(input_List), 2): #Santa for loop
        if input_List[i] == "^":
            santa_y_as += 1
        elif input_List[i] == ">":
            santa_x_as += 1
        elif input_List[i] == "v":
            santa_y_as -= 1
        else:
            santa_x_as -= 1

        santa_Position = [santa_x_as, santa_y_as]
        santa_Location.append(santa_Position)

    for i in range(1, len(input_List), 2): #Santa for loop
        if input_List[i] == "^":
            robot_y_as += 1
        elif input_List[i] == ">":
            robot_x_as += 1
        elif input_List[i] == "v":
            robot_y_as -= 1
        else:
            robot_x_as -= 1
            
        robot_Position = [robot_x_as, robot_y_as]
        robot_Location.append(robot_Position)

    amount = santa_Location + robot_Location
    amount = set(map(tuple, amount))
    amount = len(amount)
    print(amount)   
        
part_1(input)
part_2(input)