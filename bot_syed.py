def choice(round_score, my_score, opponent_score):
    ptw = 100 - my_score
    optw = 100 - opponent_score

    if optw < ptw:
        if optw <= 10:
            return round_score <= 25
        else:
            return round_score <= 18
    else:
        return round_score <= 20
