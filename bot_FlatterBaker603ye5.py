def choice(round_score, my_score, opponent_score):
    dif = opponent_score - my_score

    if (4*2**(-dif/40))+4 < random():
        return False
    elif 100 - opponent_score >= 10:
        return True
    elif dif <= -26:
        return True
    elif round_score < 20:
        return True
    else:
        return False
