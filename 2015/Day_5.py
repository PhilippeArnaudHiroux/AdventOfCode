file_Name = 'Day_5.txt'

def part_1(file_Path):
    def check(s):
        first_Check = set("aeiou")
        if sum(1 for char in s if char in first_Check) < 3:
            return False

        if not any(s[i] == s[i+1] for i in range(len(s) - 1)):
            return False

        disallowed_substrings = ["ab", "cd", "pq", "xy"]
        if any(substring in s for substring in disallowed_substrings):
            return False

        return True
    
    nice_count = 0
    with open(file_Path, 'r') as file:
        for line in file:
            if check(line.strip()):
                nice_count += 1
    print(nice_count)

def part_2(file_Path):
    with open(file_Path, 'r') as file:
        input = [line.strip() for line in file]

    def check(s):
        has_pair = False
        for i in range(len(s) - 1):
            pair = s[i:i+2]
            if s.count(pair) >= 2:
                has_pair = True
                break

        has_repeat_with_gap = any(s[i] == s[i+2] for i in range(len(s) - 2))
        return has_pair and has_repeat_with_gap

    nice_strings = [s for s in input if check(s)]
    print(len(nice_strings))

part_1(file_Name)
part_2(file_Name)
