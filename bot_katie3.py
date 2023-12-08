
def choice(round_score, my_score, opponent_score):
    if my_score == 0 and opponent_score == 0:
        return round_score <= 25
    if my_score + round_score >= 100:
        return False
    if opponent_score > 85:
        return True
    if round_score < 20:
        return True

    else:
        return False
