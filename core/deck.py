from random import randint

def build_standard_deck() -> list[dict]:
    list_deck = []
    list_suite = ['h','c','d','s']
    rank_special = ['a', 'j', 'q', 'k']
    for i in list_suite:
        r = 0
        for j in range(1 , 14):
            if 1 < j < 11:
                rank = j
            else:
                rank = rank_special[r]
                r+= 1
            list_deck.append({"rank": rank, "”suite": i})
    return list_deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    for i in range(5000):
        i = randint(0,51)
        card_i = deck[i]
        j = randint(0,51)
        card_j = deck[i]

        while not check_j(card_j ,i , j):
            j = randint(0, 51)
            card_j = deck[i]
        deck[i], deck[j] = deck[j], deck[i]

    return deck

def check_j(card_j, i, j) -> bool:
    if i == j:
        return False
    match card_j.get("rank"):
        case 'h':
            return j % 5 == 0
        case 'c':
            return j % 3 == 0
        case 'd':
            return j % 2 == 0
        case 's':
            return j % 7 == 0
    return True

