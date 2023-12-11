file_Name = "Day_1.txt"

def part_1(file_Path):
    result = 0
    number = 0
    symbol = ""
    with open(file_Path, 'r') as file:
        for line in file:
            symbol = line[:1]
            number = int(line[1:])
            if symbol == "+":
                result += number
            else:
                result -= number
    print(result)

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [int(line.strip()) for line in file]

    def check(input_List):
        current_frequency = 0
        seen_frequencies = set()

        while True:
            for change in input:
                current_frequency += change

                if current_frequency in seen_frequencies:
                    return current_frequency

                seen_frequencies.add(current_frequency)

    print(check(input))

#part_1(file_Name)
part_2(file_Name)
