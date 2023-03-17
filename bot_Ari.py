def choice(round_score, my_score, opponent_score):
    if opponent_score >= my_score:
        if round_score <= 33:
            return False
        else:
            return True
    else:
        if round_score <= 17:
            return False
        else:
            return True
