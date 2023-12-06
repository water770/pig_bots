def choice(round_score, my_score, opponent_score):
  if my_score > 71:
    return True
  if my_score > opponent_score:
    if round_score < 21 + (my_score - opponent_score) // 8:
      return True
    else:
      return False
  if my_score < opponent_score:
    if round_score < 21 + (opponent_score - my_score) // 8:
      return True
    else:
      return False
  else:
      if round_score < 21:
        return True
      else:
        return False
  return round_score <= 12
