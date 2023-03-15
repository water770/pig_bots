def choice(round_score, my_score, opponent_score):
    if round_score >= 20:
        return False
    if opponent_score - my_score < -5:
        return True
    if opponent_score == my_score:
        return True
    if opponent_score - my_score >= 5 and round_score >= 30:
        return False

