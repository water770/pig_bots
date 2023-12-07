def choice(round_score, my_score, opponent_score):

    if opponent_score == 0 and my_score == 0:
        return round_score <= 25

    if opponent_score > (my_score + 25):
        if opponent_score + 14 >= 100:
            return my_score + round_score >= 100
        return round_score <=30

    if my_score > (opponent_score + 25):
        return round_score <= 13
