def choice(round_score, my_score, opponent_score):
    if round_score > 20 + 10*opponent_score/100 or my_score + round_score >= 100:
        return False
    else:
        return True
