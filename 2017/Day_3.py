file_Path = "Day_3.txt"
with open(file_Path, 'r') as file:
    input = file.read()

def part_1(input_List):
    input_List = int(input_List)
    k = int((input_List ** 0.5 - 1) // 2) + 1
    max_val = (2 * k - 1) ** 2
    distance_Midpoint = abs((input_List - max_val) % (2 * k) - k)
    distance = k + distance_Midpoint
    print(distance)
    
part_1(input)