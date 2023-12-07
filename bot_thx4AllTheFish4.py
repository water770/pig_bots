def choice(round_score, my_score, opponent_score):
    roll = random.randint(1, 2)
    if roll == 2:
        return True
    if roll == 1:
        return False
