def choice(round_score, my_score, opponent_score):
    if opponent_score >= my_score:
        if round_score <= 45:
            return False
        else:
            return True
    else:
        if round_score <= 42:
            return False
        else:
            return True
