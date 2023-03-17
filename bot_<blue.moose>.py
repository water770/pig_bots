def choice(round_score, my_score, opponent_score):
    margin = opponent_score - my_score
    if margin < 20 and margin > -20:
        if round_score >= 20:
            return False
        else:
            return True
    if margin >= 20:
        if 100 - opponent_score <= 20:
            if my_score + round_score >= 100:
                return False
            else:
                return True
        elif round_score >= opponent_score + 10:
            return False
        else:
            return True
    if margin <= -20:
        if 100 - my_score <= 30:
            winning = 100 - my_score
            if round_score >= winning:
                return False
            else:
                return True
        elif round_score >= 15:
            return False
        else:
            return True
    if 100 - my_score <= 30:
        if round_score >= 30:
            return False
        else:
            return True
    if round_score + my_score >= 100:
        return False
