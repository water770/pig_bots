def choice(round_score, my_score, opponent_score):
  if my_score < opponent_score:
    if round_score < 20:
      return True
    else:
      return False
  if (my_score - opponent_score) > 20:
    return False
  if (opponent_score - my_score) > 15:
    return round_score >= 20
