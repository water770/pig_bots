def choice(round_score, my_score, opponent_score):
    if opponent_score == 0 and my_score == 0:
        return round_score <= 20
    elif opponent_score < 71 and my_score < 71:
        return round_score <= (21 + (abs(opponent_score - my_score))/8)
    else:
        return (my_score + round_score) < 100
