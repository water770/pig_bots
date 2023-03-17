def choice(round_score, my_score, opponent_score):
    if opponent_score > my_score:
        if round_score < 100 - my_score:
            return True
        if round_score > 100 - my_score:
             return False
    if opponent_score < my_score:
        if round_score < 100 - opponent_score:
             return True
        if round_score => 100 - opponent_score:
            return False
    if opponent_score == my_score:
        if round_score <= 100 - my_score:
            return True
        if round_score > 100 - my_score:
            return False
