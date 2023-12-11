file_Name = "Day_2.txt"

def part_1(file_Path):
    count_Two = 0
    count_Three = 0

    def check(input_string, occurrence_count):
        char_count = {}

        for char in input_string:
            char_count[char] = char_count.get(char, 0) + 1

        return any(count == occurrence_count for count in char_count.values())

    with open(file_Path, 'r') as file:
        for line in file:
            if check(line, 2):
                count_Two += 1
            if check(line, 3):
                count_Three += 1
    
    print(count_Two * count_Three)

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]
    box_count = len(input)
    
    for i in range(box_count):
        for j in range(i + 1, box_count):
            differing_indices = [index for index, (char1, char2) in enumerate(zip(input[i], input[j])) if char1 != char2]

            if len(differing_indices) == 1:
                common_letters = [char for index, char in enumerate(input[i]) if index not in differing_indices]
                print(''.join(common_letters))
                
part_1(file_Name)
part_2(file_Name)