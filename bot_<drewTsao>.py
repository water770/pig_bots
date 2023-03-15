def choice(round_score, my_score, opponent_score):
    if opponent_score > my_score:
        if round_score < (opponent_score-my_score):
            return True
        if round_score > (opponent_score-my_score):
            return False
    if opponent_score < my_score:
        if round_score < 10:
            return True
        else:
            return False
    if opponent_score == my_score:
        if round_score < 15:
            return True
        else:
            return False

    if 10 > (100-opponent_score):
        if 100 > (opponent_score+score):
            return True
        else:
            return False
