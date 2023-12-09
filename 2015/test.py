file_path = 'Day_5.txt'
with open(file_path, 'r') as file:
    input = [line.strip() for line in file]
def part_2(s):
    # Check for the pair of any two letters that appears at least twice
    has_pair = False
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if s.count(pair) >= 2:
            has_pair = True
            break

    # Check for a letter that repeats with exactly one letter between them
    has_repeat_with_gap = any(s[i] == s[i+2] for i in range(len(s) - 2))
    print(has_pair)
    print(has_repeat_with_gap)

    # String is nice if it satisfies both conditions
    return has_pair and has_repeat_with_gap

# Example usage:

nice_strings = [s for s in input if part_2(s)]

print("Number of nice strings:", len(nice_strings))