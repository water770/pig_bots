def choice(round_score, my_score, opponent_score):
    if my_score + round_score >= 100:
        return False
    if ((my_score > 70) or (opponent_score > 70)):
        return True
    hold = 21 + abs((my_score - opponent_score) / 8)
    return round_score < hold
