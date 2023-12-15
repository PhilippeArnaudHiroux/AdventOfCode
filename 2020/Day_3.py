file_Name = "Day_3.txt"

def part_1(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]

    slope_right = 3
    slope_down = 1
    width = len(input[0])
    height = len(input)
    row, col = 0, 0
    count = 0

    while row < height:
        if input[row][col] == '#':
            count += 1
        col = (col + slope_right) % width
        row += slope_down

    print(count)

def part_2(file_Path):
    def check(map_data, slope_right, slope_down):
        width = len(map_data[0])
        height = len(map_data)
        row, col = 0, 0
        tree_count = 0

        while row < height:
            if map_data[row][col] == '#':
                tree_count += 1
            col = (col + slope_right) % width
            row += slope_down

        return tree_count
    
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    result = 1

    for slope_right, slope_down in slopes:
        result *= check(input, slope_right, slope_down)

    print(result)

part_1(file_Name)
part_2(file_Name)