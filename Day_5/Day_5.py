file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = file.read()

def part_1(input_List):
    input_List = input_List.split('\n\n')
    seeds = input_List[0]
    seeds = list(map(int, seeds.split(":")[1].split()))
    maps = input_List[1:]

    for mapss in maps:
        ranges = []
        for line in mapss.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for x in seeds:
            for a, b, c in ranges:
                if b <= x < b + c:
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new

    print(min(seeds))

def part_2(input_List):
    input_List = input_List.split('\n\n')
    seeds = input_List[0]
    seeds = list(map(int, seeds.split(":")[1].split()))
    maps = input_List[1:]

    new_Seeds = []

    for i in range(0, len(seeds), 2):
        new_Seeds.append((seeds[i], seeds[i] + seeds[i + 1]))

    for mapss in maps:
        ranges = []
        for line in mapss.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(new_Seeds) > 0:
            start, end = new_Seeds.pop()
            for a, b , c in ranges:
                overlap_Start = max(start, b)
                overlap_End = min(end, b + c)
                if overlap_Start < overlap_End:
                    new.append((overlap_Start - b + a, overlap_End - b + a))
                    if overlap_Start > start:
                        new_Seeds.append((start, overlap_Start))
                    if end > overlap_End:
                        new_Seeds.append((overlap_End, end))
                    break
            else:
                new.append((start, end))
        new_Seeds = new

    print(min(new_Seeds)[0])

part_1(input)
part_2(input)