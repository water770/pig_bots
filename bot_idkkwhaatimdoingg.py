def choice(round_score, my_score, opponent_score):
    difference = opponent_score - my_score
    if (difference >= 20) or (opponent_score >= 85):
      if round_score < 20:
          return True
      if round_score >= 20:
          return False
    elif difference <= -10:
      if round_score < 10:
          return True
      if round_score >= 10:
          return False
    else:
      if round_score < 10:
        return True
      if round_score >= 10:
        return False
