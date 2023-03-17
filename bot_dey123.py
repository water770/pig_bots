def choice(round_score, my_score, opponent_score):
    if opponent_score >= my_score:
        if round_score <= 40:
            return False
        else:
            return True
    else:
        if round_score <= 25:
            return False
        else:
            return True
