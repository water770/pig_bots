def choice(round_score, my_score, opponent_score):
    if my_score <= opponent_score:
        if round_score > 22:
            return False
        if round_score <= 22:
            return True
