def choice(round_score, my_score, opponent_score):
    if my_score < opponent_score and round_score < (1.0*(opponent_score-my_score)):
        return True
    if opponent_score < my_score and round_score < 10:
        return True
    elif my_score > opponent_score and round_score > 10:
        return False
