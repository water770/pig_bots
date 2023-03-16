def choice(round_score, my_score, opponent_score):
    if my_score > opponent_score:
        if my_score - opponent_score > 12:
            if round_score < 12:
                return True
            else:
                return False
        if my_score - opponent_score <= 15:
            if round_score < 15:
                return True
            else:
                return False
    if my_score < opponent_score:
        if opponent_score >= 90:
            if round_score >= 15:
                return False
            else:
                return True
        else:
            if round_score < 15:
                return True
            else:
                return False
