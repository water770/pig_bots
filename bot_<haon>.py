def choice(round_score, my_score, opponent_score):
  diff = opponent_score - my_score # diff between human and computer
  if diff > 20:
      if round_score < 20:
          return True
      else:
          return False
  elif opponent_score > 85 and diff > 20:
      if round_score < 20:
          return True
      else:
          return False
  elif diff > 30:
      if round_score < 30:
          return True
      else:
          return False
  elif diff > 50:
      if round_score + my_score < opponent_score:
          return True
      else:
          return False
  else:
      if round_score < 20:
          return True
      else:
          return False
