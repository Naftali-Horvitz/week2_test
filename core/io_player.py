

def ask_player_action() -> str:
    res =' '
    while res not in "SH":
        res = input("type S or H\n")
    return res

