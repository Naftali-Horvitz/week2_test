from core import io_player

def calculate_hand_value(hand: list) -> int:
    sum_hand = 0
    for i in hand:
        if isinstance(i.get('rank'), int):
            sum_hand += i.get('rank')
        else:
            print(i.get('rank'))
            sum_hand += 11 if sum_hand + 11 <= 21 else 1 if i.get('rank') == 'a' else  10
    return sum_hand

def pop_deck(deck: list[dict]) -> dict:
    return deck.pop(0)

def add_card_to_player(deck, player):
    player["hand"].append(pop_deck(deck))

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:

    for i in range(2):
        player["hand"].append(pop_deck(deck))
        dealer["hand"].append(pop_deck(deck))

    print(f"value player: {calculate_hand_value(player["hand"])}")
    print(f"value dealer: {calculate_hand_value(dealer["hand"])}")

def is_over_21(deck_whom) -> bool | None:
    return calculate_hand_value(deck_whom["hand"]) > 21

def dealer_play(deck: list[dict], dealer: dict) -> bool:

    while not calculate_hand_value(dealer["hand"]) >= 17:
        dealer["hand"].append(pop_deck(deck))
    if is_over_21(dealer):
        print("dealer lost")
        return True
    return False

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    lost = False
    deal_two_each(deck, player, dealer)
    player_action = io_player.ask_player_action()
    while player_action == 'H':
        add_card_to_player(deck, player)
        calculate_hand_value(player["hand"])
        if is_over_21(player):
            print("player lost")
            lost = True
            break
        print(f"value of player: {calculate_hand_value(player["hand"])}\n")
        player_action = io_player.ask_player_action()
    if not lost:
        lost = dealer_play(deck, dealer)


    res_player = calculate_hand_value(player["hand"])
    res_dealer = calculate_hand_value(dealer["hand"])

    if not lost:
        if res_dealer == res_player:
            print("The game ended in a draw.")
        elif res_dealer >= res_player:
            print("The winner is: dealer")
        else:
            print("The winner is: player")
    print(f"result player: {res_player}\nresult dealer: {res_dealer}")

