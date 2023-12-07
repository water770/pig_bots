def choice(round_score, my_score, opponent_score):
    if my_score == opponent_score and round_score < 25:
        return True
    elif opponent_score > my_score and round_score < (opponent_score - my_score)-(opponent_score*0.20):
        return True
    else:
        return False
