file_Name = "Day_7.txt"

def part_1(file_Path):
    count = 0

    with open(file_Path, 'r') as file:
        for ip in file:
            inside_brackets = False
            abba_outside_brackets = False

            for i in range(len(ip) - 3):
                chunk = ip[i:i+4]
                if '[' in chunk:
                    inside_brackets = True
                elif ']' in chunk:
                    inside_brackets = False
                elif chunk[0] == chunk[3] and chunk[1] == chunk[2] and chunk[0] != chunk[1]:
                    if inside_brackets:
                        abba_outside_brackets = False
                        break
                    else:
                        abba_outside_brackets = True

            if abba_outside_brackets:
                count += 1

    print(count)

def part_2(file_Path):
    count = 0
    with open(file_Path, 'r') as file:
        for ip in file:
            supernet_sequences = []
            hypernet_sequences = []
            inside_brackets = False

            for i in range(len(ip)):
                if ip[i] == '[':
                    inside_brackets = True
                elif ip[i] == ']':
                    inside_brackets = False
                elif inside_brackets:
                    hypernet_sequences.append(ip[i:i+3])
                else:
                    supernet_sequences.append(ip[i:i+3])

            abas = [aba for aba in supernet_sequences if len(aba) == 3 and aba[0] == aba[2] and aba[0] != aba[1]]

            for aba in abas:
                bab = aba[1] + aba[0] + aba[1]
                if bab in hypernet_sequences:
                    count += 1
                    break

    print(count)

part_1(file_Name)
part_2(file_Name)