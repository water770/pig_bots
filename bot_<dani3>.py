def choice(round_score, my_score, opponent_score):
  if round_score < 30 or my_score + round_score > 99:
    return True
  else:
    return False
