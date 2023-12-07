def choice(round_score, my_score, opponent_score):
    if my_score >= 71 or opponent_score >= 71:
        return round_score + my_score < 100
    else:
        target_score = 21 + (abs(opponent_score - my_score)) / 8
        return round_score < target_score
