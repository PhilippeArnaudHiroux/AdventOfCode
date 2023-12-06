file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

def part_1(input_List):
    time = input_List[0]
    time = time.split(':')[1].split()
    time = [int(element) for element in time]
    distance = input_List[1]
    distance = distance.split(':')[1].split()
    distance = [int(element) for element in distance]

    result = 1
    
    for time, distance in zip(time, distance):
        time_Margin = 0
        for time_Hold in range(time):
            if time_Hold * (time - time_Hold) > distance:
                time_Margin += 1
        result *= time_Margin

    print(result)

def part_2(input_List):
    time = input_List[0].split(':')[1].replace(" ", "")
    time = ''.join(map(str, time))
    time = int(time)
    time = [time]
    distance = input_List[1].split(':')[1].replace(" ", "")
    distance = ''.join(map(str, distance))
    distance = int(distance)
    distance = [distance]

    result = 1
    
    for time, distance in zip(time, distance):
        time_Margin = 0
        for time_Hold in range(time):
            if time_Hold * (time - time_Hold) > distance:
                time_Margin += 1
        result *= time_Margin

    print(result)

part_1(input)
part_2(input)