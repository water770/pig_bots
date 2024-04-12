def choice(round_score, my_score, opponent_score):
    total_score = my_score + round_score
    score_difference = total_score - opponent_score
    if total_score >= 100:
        return False
    elif opponent_score >= 90:
        return True
    elif score_difference <= -40:
        return round_score < 35
    elif -40 < score_difference <= -20:
        return round_score < 30
    elif -20 < score_difference <= 0:
        return round_score < 25
    elif 0 < score_difference <= 20:
        return round_score < 20
    elif 20 < score_difference <= 40:
        return round_score < 15
    else:
        return round_score < 10
