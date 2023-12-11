from collections import Counter

file_Name = "Day_4.txt"

def part_1(file_Path):
    result = 0
    with open(file_Path, 'r') as file:
        for line in file:
            line = line.split()
            if len(line) == len(set(line)):
                result += 1

    print(result)

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input_data = file.read()

    input_data = input_data.split("\n")

    count = 0
    for passphrase in input_data:
        words = passphrase.split()
        word_counts = [Counter(word) for word in words]

        # Check if there are any anagrams
        for i, word_count in enumerate(word_counts):
            for j, other_word_count in enumerate(word_counts):
                if i != j and word_count == other_word_count:
                    break
            else:
                continue
            break
        else:
            count += 1

    print(count)

part_1(file_Name)
part_2(file_Name)


