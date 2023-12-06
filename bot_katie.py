
def choice(round_score, my_score, opponent_score):
    if my_score == 0 and opponent_score == 0:
        return round_score <= 40
    if round_score < 15:
        return True
    if opponent_score > 85 & opponent_score - my_score > 40:
        return True
    if opponent_score + round_score > 100:
        return False
    else:
        return False
