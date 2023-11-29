def choice(round_score, my_score, opponent_score):
    if (my_score >= 71) or (opponent_score >= 71):
        return round_score >= (100 - my_score)
    else:
        return round_score >= (21 + (abs(my_score - opponent_score)/8)

# 0.9% Disadvantage against Optimal Play. Read the Wikipedia article on Pig for more info.
