def choice(round_score, my_score, opponent_score):
  if my_score > 90:
    if round_score + my_score < 100:
        return True
    else:
        return False
  elif opponent_score > my_score and opponent_score < 45:
    if round_score < 15:
        return True
    else:
        return False
  elif opponent_score > my_score and opponent_score < 75:
    if round_score < 25:
        return True
    else:
        return False
  elif opponent_score > my_score and opponent_score > 75 and opponent_score < 90:
    if round_score < 30 or round_score + my_score > 99:
        return True
    else:
        return False
  elif opponent_score > my_score and opponent_score > 80:
    if round_score + my_score > 99:
        return True
    else:
        return False
  else:
    if round_score < 20 or round_score + my_score > 99:
        return True
    else:
        return False
