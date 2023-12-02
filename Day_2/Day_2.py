file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

def part_1(input_List):
    new_List = [game for game in input_List if not any(int(part) > 12 for part in game.split() if part.isdigit() and 'red' in game.split())]
    new_List = [game for game in new_List if not any(int(part) > 13 for part in game.split() if part.isdigit() and 'green' in game.split())]
    new_List = [game for game in new_List if not any(int(part) > 14 for part in game.split() if part.isdigit() and 'blue' in game.split())]
    new_List = [game.split(':')[0] for game in input_List]
    new_List = [game.replace('Game ', '') for game in new_List]
    new_List = [int(game) for game in new_List]
    result = sum(new_List)

    print(result)

def part_2(input_List):
    # part 2
    result = 0
    for input in input_List:
        input = input.split(':')[1].split(';')
        colors = [0, 0, 0]
        for game in input:
            game = game.strip().split(',')
            for game in game:
                game = game.strip().split(' ')
                if game[1] == 'green' and int(game[0]) > colors[1]:
                    colors[1] = int(game[0])
                if game[1] == 'red' and int(game[0]) > colors[0]:
                    colors[0] = int(game[0])
                if game[1] == 'blue' and int(game[0]) > colors[2]:
                    colors[2] = int(game[0])
        
        result += (colors[0]*colors[1]*colors[2])
    print(result)


#part_1(input)
part_2(input)



