def choice(round_score, my_score, opponent_score):
    if ((my_score >= 60) and (my_score + round_score < 100)):
        return my_score + round_score < 100
    else:
         hold = 22 + (my_score - opponent_score) if opponent_score < my_score else 22 + (opponent_score - my_score)
    return round_score < hold
