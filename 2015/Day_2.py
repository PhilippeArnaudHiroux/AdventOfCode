file_path = 'Day_2.txt'
with open(file_path, 'r') as file:
    input = file.read()

def part_1(input_List):
    input_List = input_List.split()
    input_List = [item.split('x') for item in input_List]
    input_List = [[int(num) for num in sublist] for sublist in input_List]

    result = 0

    for i in range(len(input_List)):
        lw =  input_List[i][0] * input_List[i][1]
        wh = input_List[i][1] * input_List[i][2]
        hl = input_List[i][0] * input_List[i][2]

        if lw < wh and lw < hl:
            result += 2 * lw + 2 * wh + 2 * hl + lw
            print("0")
        if wh < lw and wh < hl:
            result += 2 * lw + 2 * wh + 2 * hl + wh
            print("1")
        if hl < lw and hl < wh:
            result += 2 * lw + 2 * wh + 2 * hl + hl
            print("2")

        print(result)

part_1(input)