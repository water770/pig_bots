def choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100:
        return False
    if opponent_score - my_score > 30:
        return round_score <= 40
    if my_score - opponent_score < 0:
        return round_score <= 15
    if round_score <= 20:
        return True
    else:
        return False
