def choice(round_score, my_score, opponent_score):
    if opponent_score >= my_score:
        if round_score >= 38:
            return False
        else:
            return True
    else:
        if round_score >= 24:
            return False
        else:
            return True
