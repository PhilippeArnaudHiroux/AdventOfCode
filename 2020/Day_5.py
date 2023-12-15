file_Name = "Day_5.txt"

def  part_1(file_Path):
    def check(boarding_pass):
        row_min, row_max = 0, 127
        col_min, col_max = 0, 7

        for char in boarding_pass:
            if char == 'F':
                row_max = (row_min + row_max) // 2
            elif char == 'B':
                row_min = (row_min + row_max) // 2 + 1
            elif char == 'L':
                col_max = (col_min + col_max) // 2
            elif char == 'R':
                col_min = (col_min + col_max) // 2 + 1

        row = row_min
        col = col_min
        seat_id = row * 8 + col
        return seat_id

    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]

    print(max(check(boarding_pass) for boarding_pass in input))

part_1(file_Name)