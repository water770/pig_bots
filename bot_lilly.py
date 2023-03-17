def choice(round_score,my_score, opponent_score)
      num = 21
  ##if opponent_score - my_score >= 30:
           ##num = 26
      if my_score + round_score >=100:
          return False
      if opponent_score > 85 and my_score + round_score<100 and round_score< 45:
          return True
      if round_score < num:
          return True
      if round_score>num:
          return False
