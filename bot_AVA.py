def choice(round_score, my_score, opponent_score):
    difference = abs(opponent_score - my_score)
    if round_score < 17:
        return True
    elif my_score > 75 and difference < 10:
        return round_score < 25
    elif opponent_score > 90:
        return round_score < 25
    while my_score >= 70:
        return my_score + round_score < 100
