def choice(round_score, my_score, opponent_score):
  if opponent_score > 80 and  opponent_score > my_score:
      if round_score < 100 - my_score:
          return True
      else:
          return False
  elif my_score > 80:
      if round_score < 100 - my_score:
          return True
      else:
          return False
  else:
      if round_score < 20:
          return True
      else:
          return False
    
  
