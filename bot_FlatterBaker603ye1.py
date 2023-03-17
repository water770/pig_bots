def choice(round_score, my_score, opponent_score):
    fun = 1
    set_fun = fun
    if round_score + my_score == my_score:
        tim = 0
    tim += 1
    
    dif = opponent_score - my_score

    if (dif >= 20) or (dif <= -26):
        fun -= 0.11
        if (dif >= 35) or (dif <= -41):
            fun -= 0.22
            if (dif >= 45) or (dif <= -51):
                fun -= 0.44
    else:
        fun = set_fun

        
    if round_score < 20:
        if fun > random():
            if 2*(2**(-tim/4)) < random():
                tim = 0
                return False
            else:
                return True
