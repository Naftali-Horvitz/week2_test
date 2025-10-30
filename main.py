from core import deck, logic_game




if __name__ == "__main__":
    deck1 = deck.build_standard_deck()
    deck1 = deck.shuffle_by_suit(deck1)
    player = {"hand": []}
    dealer = {"hand": []}
    logic_game.run_full_game(deck1, player, dealer)
