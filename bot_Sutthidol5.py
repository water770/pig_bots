def choice(round_score, my_score, opponent_score):
      if my_score > 70 and opponent_score + 30 < my_score:
        if round_score < 20:
            return True
      elif round_score > 20:
        return False
      elif opponent_score > my_score + 20:
          if round_score < 25:
              return True
      elif opponent_score > my_score + 10:
          if round_score < 20:
              return True
      elif my_score + round_score >= 100:
          return False
      elif opponent_score < 40 and my_score + round_score > 80:
          return False
      if my_score < 10 and opponent_score < 30:
          if round_score < 20:
              return True
