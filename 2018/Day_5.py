file_Name = "Day_5.txt"

def part_1(file_Path):
    def check(input_Str):
        i = 0
        while i < len(input_Str) - 1:
            if abs(ord(input_Str[i]) - ord(input_Str[i + 1])) == 32:
                input_Str = input_Str[:i] + input_Str[i + 2:]
                i = max(0, i - 1)
            else:
                i += 1
        return input_Str
    
    with open(file_Path, 'r') as file:
        input = file.read()

    length = len(input) + 1
    while len(input) < length:
        length = len(input)
        polymer = check(input)

    print(len(polymer))

def part_2(file_Path):
    def fully_react(polymer):
        prev_length = len(polymer) + 1
        while len(polymer) < prev_length:
            prev_length = len(polymer)
            i = 0
            while i < len(polymer) - 1:
                if abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32:
                    polymer = polymer[:i] + polymer[i + 2:]
                    i = max(0, i - 1)
                else:
                    i += 1
        return polymer
    
    with open(file_Path, 'r') as file:
        input = file.read()
    
    unit_types = set(input.lower())
    shortest = float('inf')

    for unit_type in unit_types:
        modified = input.replace(unit_type.lower(), '').replace(unit_type.upper(), '')
        reacted = fully_react(modified)
        shortest = min(shortest, len(reacted))

    print(shortest)

part_1(file_Name)
part_2(file_Name)
