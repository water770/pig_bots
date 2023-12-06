def choice(round_score, my_score, opponent_score):
    if my_score == 0 and opponent_score == 0:
        return round_score <= 25
    elif my_score <= 71:
        return round_score < (21 + (opponent_score - my_score)/8)
    else:
        return (round_score + my_score) < 100
