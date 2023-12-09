file_Name = 'Day_9.txt'

def part_1(file_Path):
    def extrapolate(list):
        if all(x == 0 for x in list):
            return 0

        deltas = [y - x for x, y in zip(list, list[1:])]
        diff = extrapolate(deltas)
        return list[-1] + diff

    total = 0

    for line in open(file_Path, 'r'):
        nums = list(map(int, line.split()))
        total += extrapolate(nums)

    print(total)

def part_2(file_Path):
    def extrapolate(list):
        if all(x == 0 for x in list):
            return 0

        deltas = [y - x for x, y in zip(list, list[1:])]
        diff = extrapolate(deltas)
        return list[0] - diff

    total = 0

    for line in open(file_Path, 'r'):
        nums = list(map(int, line.split()))
        total += extrapolate(nums)

    print(total)

part_1(file_Name)
part_2(file_Name)
