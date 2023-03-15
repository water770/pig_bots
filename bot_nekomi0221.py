def choice(round_score, my_score, opponent_score):
  if my_score <= opponent_score:
    if round_score <= 24:
      return True
    else:
      return False
  if my_score > opponent_score:
    if round_score <= 12:
      return True
    else:
      return False
