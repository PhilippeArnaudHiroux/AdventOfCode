file_Name = "Day_3.txt"

def part_1(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
    fabric = [[0] * 1000 for _ in range(1000)]

    for claim in input:
        claim_id, _, start, size = claim.split()
        x, y = map(int, start[:-1].split(','))
        width, height = map(int, size.split('x'))

        for i in range(x, x + width):
            for j in range(y, y + height):
                fabric[i][j] += 1

    inches = sum(1 for row in fabric for inch in row if inch > 1)

    print(inches)

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
    fabric = [[0] * 1000 for _ in range(1000)]
    claim_status = {}

    for claim in input:
        claim_id, _, start, size = claim.split()
        x, y = map(int, start[:-1].split(','))
        width, height = map(int, size.split('x'))

        claim_status[claim_id] = True
        for i in range(x, x + width):
            for j in range(y, y + height):
                if fabric[i][j] == 0:
                    fabric[i][j] = claim_id
                else:
                    claim_status[claim_id] = False
                    claim_status[fabric[i][j]] = False

    non_overlapping_claim = next(claim for claim, status in claim_status.items() if status)
    print(non_overlapping_claim)

part_1(file_Name)
part_2(file_Name)