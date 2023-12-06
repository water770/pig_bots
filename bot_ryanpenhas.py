def choice(round_score, my_score, opponent_score):
    if my_score >= 90:
        return round_score <= 5
    else:
        return round_score <= 10
