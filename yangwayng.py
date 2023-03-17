def choice(round_score, my_score, opponent_score):
    if my_score <= opponent_score:
        if round_score >= 28:
            return True
    if my_score > opponent_score:
        if round_score <= 14:
            return True
        else:
            return False
