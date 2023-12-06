def choice(round_score, my_score, opponent_score):
    if (my_score >= 95) or (opponent_score >= 95):
        return True
    elif round_score <= 24:
        return True
    else:
        return False
