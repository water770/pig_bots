def choice(round_score, my_score, opponent_score):
    if 100 - opponent_score <=20 or 100 - my_score <= 20:
        if round_score >= 100 - my_score:
            return False
        else:
            return True
    else:
        if round_score < 20:
            return True
        else:
            return False
