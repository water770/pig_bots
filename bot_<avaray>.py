def choice(round_score, my_score, opponent_score):
    if (opponent_score - my_score) > 20:
        return round_score <= 20
    else:
        return round_score <= 15
    
