def choice(round_score, my_score, opponent_score):
    if my_score >= opponent_score:
        return round_score >= 12
    elif my_score < opponent_score:
        return round_score >= 69420
