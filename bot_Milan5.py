def choice(round_score, my_score, opponent_score):
    if opponent_score >=75 or my_score >= 75:
        if my_score >= 75:                        #if im close to winning
            if round_score >= 100 - my_score:     #stop if my round_score will get me to win
                return False
            if round_score < 100 - my_score:
                return True

        if opponent_score >=75:                   #if opponent is close winning
            if my_score >= 65:                    #if im close behind, risk it to go for win
                if round_score < 35:
                    return True
                else:
                    return False
            else:                                   #if im not close behind
                if round_score + my_score >=75:     #risk it and try to match opponent's score
                    return False
                else:
                    return True
    else:                                           #if neither of us are close to winning
        if round_score < 20:                        #go for at least 20 each round
            return True
        else:
            return False
