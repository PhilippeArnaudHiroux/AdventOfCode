file_path = 'input.txt'
with open(file_path, 'r') as file:
    input = [line.strip() for line in file]

def part_1(input):
    cs = set()

    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for dr in range(r - 1, r + 2):
                for dc in range(c - 1, c + 2):
                    if dr < 0 or dr >= len(input) or dc < 0 or dc >= len(input[dr]) or not input[dr][dc].isdigit():
                        continue
                    while dc > 0 and input[dr][dc - 1].isdigit():
                        dc -= 1
                    cs.add((dr, dc))

    ns = []

    for r, c in cs:
        s = ""
        while c < len(input[r]) and input[r][c].isdigit():
            s += input[r][c]
            c += 1
        ns.append(int(s))

    print(sum(ns))

def part_2(input):
    total = 0

    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            if ch != "*":
                continue

            cs = set()
            
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr >= len(input) or cc < 0 or cc >= len(input[cr]) or not input[cr][cc].isdigit():
                        continue
                    while cc > 0 and input[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))
                    
            if len(cs) != 2:
                continue

            ns = []

            for cr, cc in cs:
                s = ""
                while cc < len(input[cr]) and input[cr][cc].isdigit():
                    s += input[cr][cc]
                    cc += 1
                ns.append(int(s))
            
            total += ns[0] * ns[1]

    print(total)
part_1(input)
part_2(input)
