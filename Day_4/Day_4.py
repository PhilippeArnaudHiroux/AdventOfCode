file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

def part_1(input_List):
    input_List = [game.split(':')[-1] for game in input_List]
    count = 0

    for input_String in input_List:
        lists = input_String.split('|')
        winning_Numbers = [int(num) for num in lists[0].strip().split()]
        your_Numbers = [int(num) for num in lists[1].strip().split()]
        same_Numbers = len(set(winning_Numbers).intersection(your_Numbers))
        result = 2**(same_Numbers-1)
        if result >= 1:
            count += result
    
    print(count)

def part_2(input_List):
    input_List = [game.split(':')[-1] for game in input_List]
    output_List = {}

    for count, input_String in enumerate(input_List):
        lists = input_String.split('|')
        winning_Numbers = [int(num) for num in lists[0].strip().split()]
        your_Numbers = [int(num) for num in lists[1].strip().split()]
        same_Numbers = len(set(winning_Numbers).intersection(your_Numbers))
        
        if count not in output_List:
            output_List[count] = 1
        
        for z in range(count +1, count + same_Numbers + 1):
                output_List[z] = output_List.get(z, 1) + output_List[count]

    print(sum(output_List.values()))
    
part_1(input)
part_2(input)


