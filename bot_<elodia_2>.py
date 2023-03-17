def choice(round_score, my_score, opponent_score):
  if my_score + round_score >= 100:
    return False
  return round_score <= 20
