def choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100:
        return False
    elif my_score + round_score >= 85 and round_score <= 20:
        return True
    elif round_score <= 25 and opponent_score - (my_score + round_score) >= 20:
        return True
    elif round_score <= 17:
        return True
    return False
