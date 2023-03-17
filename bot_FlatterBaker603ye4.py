def choice(round_score, my_score, opponent_score):
    dif = opponent_score - my_score

    if (100 - opponent_score) < 10:
        return True
    elif dif >= 10:
        return True
    elif dif <= -26:
        return False
    elif round_score < dif or round_score < 20:
        return True
    else:
        return False
