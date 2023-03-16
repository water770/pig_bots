def choice(round_score, my_score, opponent_score):
  if my_score > 70 and opponent_score +40 < my_score:
    if round_score < 15:
      return True
    elif round_score > 15:
      return False
  if opponent_score > my_score + 20:
    if round_score < 30:
      return True
    if opponent_score > my_score:
      if round_score < 20:
        return True
    
