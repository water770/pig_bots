def choice(round_score, my_score, opponent_score):
    if ((my_score > 70) or (opponent_score > 70)) and (my_score + round_score < 100):
        return my_score + round_score < 100
    else:
        hold = 21 + ((my_score - opponent_score) / 8) if my_score > opponent_score else 21 + ((opponent_score - my_score) / 8)
        return round_score < hold
