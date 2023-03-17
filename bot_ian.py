def choice(round_score, my_score, opponent_score):
  if opponent_score > my_score:
    if round_score < 17:
      return True
    else:
      return False
  if opponent_score < my_score:
    if round_score < 12:
      return True
    else:
      return False
  if opponent_score == my_score:
    if round_score < 14:
      return True
    else:
      return False
  
