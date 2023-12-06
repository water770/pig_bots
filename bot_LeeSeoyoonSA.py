def choice(round_score, my_score, opponent_score):
    if opponent_score == 0 and my_score == 0:
        return round_score <= 21
    elif opponent_score < 70 and my_score < 70:
        return round_score <= 10
    else:
        return True
