#tuning tuning tuning
def choice(round_score, my_score, opponent_score):
    difference = opponent_score - my_score
    if difference > 0:
        threshold = round(pow(22, (difference + 20)/77)+20)
    elif difference <= 0:
        threshold = 23.5
    #keep the lines bellow
    if round_score + my_score >= 100:
        return False
    if round_score <= threshold:
        return True
    elif round_score > threshold:
        return False
