def choice(round_score, my_score, opponent_score):
    if my_score == opponent_score == 0:
        return round_score <= 22
    if my_score + 20 > opponent_score:
        return round_score <= 15
    if opponent_score + 20 > my_score:
        if opponent_score + 10 >= 100:
            return my_score + round_score >= 100
        else:
            return round_score 30
