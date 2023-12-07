def choice(round_score, my_score, opponent_score):
    if my_score + round_score <= opponent_score:
        return True
    if my_score + round_score >= opponent_score + (opponent_score)/10:
        return True
    else:
        return False
