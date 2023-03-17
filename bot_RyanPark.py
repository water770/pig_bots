def choice(round_score, my_score, opponent_score):
    difference = opponent_score - my_score
    if difference > 0:
        threshold = round(pow(45, (difference + 10)/82)+15.2)
    elif difference <= 0:
        threshold = 15
    if round_score + my_score >= 100:
        return False
    if round_score <= threshold:
        return True
    elif round_score > threshold:
        return False
