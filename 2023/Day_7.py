file_path = 'Day_7.txt'
with open(file_path, 'r') as file:
    input = file.read()

def part_1(input_List):
    letter_Maping = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
    def classify(hand):
        counts = [hand.count(card) for card in hand]

        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def strength_Hand(hand):
        return (classify(hand), [letter_Maping.get(card, card) for card in hand])
    
    input_List = input_List.split("\n")
    input_List = [string.split(" ") for string in input_List]
    input_List = [[sublist[0], int(sublist[1])] for sublist in input_List]
    
    input_List.sort(key=lambda play: strength_Hand(play[0]))    

    result = 0

    for ranking, (hands, bids) in enumerate(input_List, 1):
        result += ranking * bids
    print(result)

def part_2(input_List):
    letter_Maping = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

    def score(hand):
        counts = [hand.count(card) for card in hand]

        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def replacements(hand):
        if hand == "":
            return [""]

        return [
            x + y
            for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
            for y in replacements(hand[1:])
        ]

    def classify(hand):
        return max(map(score, replacements(hand)))

    def strength_Hand(hand):
        return (classify(hand), [letter_Maping.get(card, card) for card in hand])
    
    input_List = input_List.split("\n")
    input_List = [string.split(" ") for string in input_List]
    input_List = [[sublist[0], int(sublist[1])] for sublist in input_List]
    
    input_List.sort(key=lambda play: strength_Hand(play[0]))    

    result = 0

    for ranking, (hands, bids) in enumerate(input_List, 1):
        result += ranking * bids
    print(result)
    
part_1(input)
part_2(input)
