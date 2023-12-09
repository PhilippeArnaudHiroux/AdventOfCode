def part_1(file_path):
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
    with open(file_path, 'r') as file:
        for line in file:
            if check(line.strip()):
                nice_count += 1
    return nice_count

# Replace 'your_file_path.txt' with the actual path to your text file
file_path = 'Day_5.txt'
count = part_1(file_path)
print(count)