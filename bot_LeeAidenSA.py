def choice(round_score, my_score, opponent_score):
    threshold = 25 + (opponent_score - my_score) / 10
    if my_score + round_score >= 100:
        threshold = 5
    return round_score < threshold
