def choice(round_score, my_score, opponent_score):
    hold_calc = round(21 + (abs((my_score - opponent_score)/8)), 2)
    if round_score <= hold_calc:
        return True
    else:
        return False
