def choice(round_score, my_score, opponent_score):
    if opponent_score - my_score >= 20:
        if round_score > 20:
            return False
        else:
            return True
    if 0 < (opponent_score - my_score) < 5:
        return False
    elif my_score > 90:
        if 95 < my_score < 98:
            return False
        else:
            return True
    elif round_score > 20:
        return False
    elif round_score < 20:
        return True
