def choice(round_score,my_score, opponent_score):
       num = 25
       if my_score[0] + round_score >=100:
            return False
       if opponent_score > 85 and my_score + round_score<100 and round_score< 45:
            return True
       if round_score < num:
           return True
       if round_score>num:
           return False
