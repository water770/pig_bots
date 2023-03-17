def choice(round_score, my_score, opponent_score):
    if my_score <= opponent_score:
        if round_score >= 20:
            return True
        else:
            return Flase
    if my_score > opponent_score:
        if round_score <= 28:
            return True
        else:
            return False
