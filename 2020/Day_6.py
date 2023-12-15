file_Name = "Day_6.txt"

def part_1(file_Path):
    with open(file_Path, "r") as file:
        groups = file.read().split('\n\n')

    result = 0

    for group in groups:
        answers = group.split('\n')
        group_answers = set(''.join(answers))
        result += len(group_answers)

    print(result)

def part_2(file_Path):
    with open(file_Path, "r") as file:
        groups = file.read().split('\n\n')

    result = 0

    for group in groups:
        answers = group.split('\n')
        if not answers:
            continue
        group_answers = set(answers[0]).intersection(*answers[1:])
        result += len(group_answers)

    print(result)

part_1(file_Name)
part_2(file_Name)