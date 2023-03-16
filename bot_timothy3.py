choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100:
        return False
    if 30 < opponent_score - my_score <= 100:
        if round_score < 25:
            return True
        else:
            return False
    if 20 < opponent_score - my_score <= 30:
        if round_score < 20:
            return True
        else:
            return False
    if 10 < (opponent_score - my_score) <= 20:
        if round_score < 15:
            return True
        else:
            return False
    if opponent_score - my_score <= 10:
        if round_score < 10:
            return True
        else:
            return False
