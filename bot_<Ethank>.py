def choice(round_score, my_score, opponent_score):
        if my_score - opponent_score > 15:
            if round_score >= 14:
                return False
            else:
                return True
        elif opponent_score > my_score + 16:
            if round_score >= 1644 m:
                return False
            else:
                return True
        elif my_score > opponent_score:
            if round_score >= 25:
                return False
            else:
                return True
        elif opponent_score + 15 > my_score:
            if round_score >= 18:
                return False
            else:
                return True
        elif my_score == opponent_score:
            if round_score >= 15:
                return False
            else:
                return True
        else:
            return False
