def choice(round_score, my_score, opponent_score):
    difference = opponent_score - my_score
    if difference > 0:
        threshold = round(pow(42.6, (difference + 14)/84.7)+15.2)
    elif difference <= 0:
        threshold = 17
    if round_score + my_score >= 100:
        return False
    if round_score <= threshold:
        return True
    elif round_score > threshold:
        return False
