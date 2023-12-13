file_Name = "Day_2.txt"

def part_1(file_Path):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    position = (1, 1)

    code = []
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
        for line in input:
            for move in line:
                if move == 'U' and position[0] > 0:
                    position = (position[0] - 1, position[1])
                elif move == 'D' and position[0] < 2:
                    position = (position[0] + 1, position[1])
                elif move == 'L' and position[1] > 0:
                    position = (position[0], position[1] - 1)
                elif move == 'R' and position[1] < 2:
                    position = (position[0], position[1] + 1)

            code.append(keypad[position[0]][position[1]])

    print(''.join(map(str, code)))

def part_2(file_Path):
    keypad = [
        [' ', ' ', '1', ' ', ' '],
        [' ', '2', '3', '4', ' '],
        ['5', '6', '7', '8', '9'],
        [' ', 'A', 'B', 'C', ' '],
        [' ', ' ', 'D', ' ', ' ']
    ]
    current_button = (2, 0)  # Start at button "5" (coordinates are 0-indexed)

    code = []
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
        for line in input:
            for move in line:
                row, col = current_button

                if move == 'U' and row > 0 and keypad[row - 1][col] != ' ':
                    current_button = (row - 1, col)
                elif move == 'D' and row < 4 and keypad[row + 1][col] != ' ':
                    current_button = (row + 1, col)
                elif move == 'L' and col > 0 and keypad[row][col - 1] != ' ':
                    current_button = (row, col - 1)
                elif move == 'R' and col < 4 and keypad[row][col + 1] != ' ':
                    current_button = (row, col + 1)

            code.append(keypad[current_button[0]][current_button[1]])

    print(''.join(code))

part_1(file_Name)
part_2(file_Name)