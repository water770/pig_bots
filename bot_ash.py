def choice(round_score, my_score, opponent_score):
    if my_score <= 12:
        return True
    elif (opponent_score - my_score) >= 20:
        return True
    elif my_score >= 80:
        return True
    elif round_score > 25:
        return False
    else:
        return False
