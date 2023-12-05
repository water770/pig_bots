def choice(round_score, my_score, opponent_score):
    if round_score + my_score >=100:
        return False
    elif opponent_score >= round_score+my_score+20:
        return True
    elif (opponent_score > 75) or (my_score + round_score >80):
        return True
    elif round_score < 23:
        return True
    else:
        return False
