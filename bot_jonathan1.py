def choice(round_score, my_score, opponent_score):
    if my_score + round_score > 100:
        return False
    if my_score + round_score < 15:
        if round_score < 20:
            return True
        else:
            return False
    if my_score + round_score < 80:
        if round_score < 20:
            return True
        else:
            return False
    if my_score + round_score + 10 < opponent_score:
        if round_score < 24:
            return True
        else:
            return False
    if my_score + round_score + 20 < opponent_score:
        if round_score < 27:
            return True
        else:
            return False
    if my_score + round_score >= opponent_score + 20:
        if round_score < 15:
            return True
        else:
            return False
    if my_score + round_score > opponent_score + 10:
        if round_score < 18:
            return True
        else:
            return False
