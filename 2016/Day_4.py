import re
from collections import Counter

file_Name = "Day_4.txt"

def part_1(file_Path):
    def check(name, sector_id, checksum):
        letter_counts = Counter(name.replace('-', ''))
        sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
        calculated_checksum = ''.join(letter for letter, _ in sorted_letters[:5])
        return calculated_checksum == checksum
    
    with open(file_Path, 'r') as file:
        input = file.read().strip().split('\n')

    result = 0

    for room in input:
        match = re.match(r'([a-z-]+)-(\d+)\[([a-z]+)\]', room)
        encrypted_name, sector_id, checksum = match.groups()

        if check(encrypted_name, int(sector_id), checksum):
            result += int(sector_id)

    print(result)

part_1(file_Name)