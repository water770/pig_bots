def choice(round_score, my_score, opponent_score):
    seeds = [1, 7, 10, 5, 19]
    random.seed(round_score * (opponent_score + 1))
    random.seed(seeds[random.randint(0, 4)])
    if round_score >= 100:
        return False
    return True
