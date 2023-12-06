def choice(round_score, my_score, opponent_score):
     if (my_score == 0) or (opponent_score == 0):
         return round_score <= 20
     mywin = 100 - (my_score + round_score)
     oppwin = 100 - (opponent_score + round_score)
     if (oppwin <= 20) and (mywin > 30) and (my_score + round_score < 100):
         if (oppwin <= 6):
            return round_score + my_score == 100
         else:
            return round_score <= 26
     if (mywin <= 25) or (oppwin <= 25) and (my_score + round_score < 100):
         return round_score <= 10
     else:
         return False
