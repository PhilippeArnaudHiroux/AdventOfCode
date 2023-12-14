file_Name = "Day_1.txt"

def part_1(file_Path):
    with open(file_Path, 'r') as file:
        input = file.read().replace(" ", "").split(",")
    x, y = 0, 0
    direction = 0

    for instruction in input:
        turn, distance = instruction[0], int(instruction[1:])
        
        if turn == 'R':
            direction = (direction + 1) % 4
        elif turn == 'L':
            direction = (direction - 1) % 4

        if direction == 0:
            y += distance
        elif direction == 1:
            x += distance
        elif direction == 2:
            y -= distance
        elif direction == 3:
            x -= distance

    print(abs(x) + abs(y))

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = file.read().replace(" ", "").split(",")
    x, y = 0, 0
    direction = 0
    visited_locations = set()
    visited_locations.add((x, y))

    for instruction in input:
        turn, distance = instruction[0], int(instruction[1:])
        
        if turn == 'R':
            direction = (direction + 1) % 4
        elif turn == 'L':
            direction = (direction - 1) % 4

        for _ in range(distance):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1

            if (x, y) in visited_locations:
                return abs(x) + abs(y)
            
            visited_locations.add((x, y))

part_1(file_Name)
print(part_2(file_Name))
