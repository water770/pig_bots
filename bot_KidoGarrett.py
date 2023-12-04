def choice(round_score, my_score, opponent_score):
  if 100 - (my_score + round_score) <= 0:
    return False
  elif my_score - opponent_score > 25:
    return round_score <= 15
  elif opponent_score - my_score > 25:
    return round_score <= 25
  else:
    return round_score <= 20
