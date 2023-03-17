def choice(round_score, my_score, opponent_score):
    dif = opponent_score - round_score
    hold = min(round((4.49099 ** ((0.0122656 * dif) + 2.10924)) - 3.7654), 100 - round_score)
    if my_score <= hold:
        return True
    else:
        return False
