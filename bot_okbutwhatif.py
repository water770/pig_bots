def choice(round_score, my_score, opponent_score):
    if my_score < 15:
        return True
    elif (opponent_score - my_score) > 20:
        return True
    elif (my_score - opponent_score) >= 15:
        return False
    elif opponent_score >= 85 and my_score <= 60:
        return True
    elif round_score > 20:
        return False
    else:
        return False
