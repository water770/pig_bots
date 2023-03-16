def choice(round_score, my_score, opponent_score):
  if round_score < 14:
    return True
  if round_score > 6:
    return False
  
  elif (opponent_score - my_score) > 10:
    return True
  elif (my_score = opponent_score) >= 14:
    return False
