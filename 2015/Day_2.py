file_Name = "Day_2.txt"

def part_1(file_Path):
    result = 0
    with open(file_Path, 'r') as file:
        input = file.read()

    input = input.split('\n')
    input = [list(map(int, row.split('x'))) for row in input]

    for dimensions in input:
        l, w, h = dimensions
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l
        smallest_side_area = min(l * w, w * h, h * l)
        result += surface_area + smallest_side_area

    print(result)

def part_2(file_Path):
    result = 0
    with open(file_Path, 'r') as file:
        input = file.read()

    input = input.split('\n')
    input = [list(map(int, row.split('x'))) for row in input]

    for dimensions in input:
        l, w, h = dimensions
        perimeter = 2 * min(l + w, w + h, h + l)
        bow_ribbon = l * w * h
        result += perimeter + bow_ribbon

    print(result)

part_1(file_Name)
part_2(file_Name)
