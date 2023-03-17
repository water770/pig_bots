def choice(c,p,o):
    def score(x):
        low=0
        medium=0
        high=0
        very_high=0
        if 0<=x<5:
            low=1
        elif 5<=x<15:
            low = -0.1*x+2
        if 15<=x<25:
            medium=0.1*x-2.5
        elif 25<=x<60:
            medium = 1
        elif 55<=x<65:
            medium = -0.1*x+6.5

        if 60<=x<65:
            high=0.1*x-6
        elif 65<=x<75:
            high=1
        elif 75<=x<85:
            high=-0.1*x+8.5
        if 75<=x<85:
            very_high=0.1*x-7.5
        elif 85<=x<100:
            very_high=1
        return [low,medium,high,very_high]
    def score2(x):
        low=0
        medium=0
        high=0
        very_high=0
        if 0<=x<5:
            low=1
        elif 5<=x<15:
            low = -0.1*x+1.5
        if 20<=x<30:
            medium=0.1*x-2
        elif 30<=x<60:
            medium = 1
        elif 55<=x<65:
            medium = -0.1*x+6.5
        if 55<=x<65:
            high=0.1*x-5
        elif 65<=x<75:
            high=1
        elif 75<=x<85:
            high=-0.1*x+8.5
        if 75<=x<85:
            very_high=0.1*x-7.5
        elif 85<=x<100:
            very_high=1
        return [low,medium,high,very_high]

    def roundScore(x):
        low=0
        medium=0
        high=0
        very_high=0
        if 0<=x and x<13:
            low=1
        elif 13<=x and x<=18:
            low=-0.2*x+(18/5)
        if 10<=x and x<15:
            medium=0.2*x-2
        elif 15<=x and x<15:
            medium=1
        elif 15<=x<20:
            medium=-0.2*x+(20*0.2)
        if 12<=x and x<20:
            high=0.2*x+4
        elif 20<=x and x<25:
            high=1
        elif 25<=x and 30<x:
            high=-0.2*x+6
        if 20<=x and x<=25:
            very_high=0.2*x-4
        elif x>25:
            very_high=1
        return [low,medium,high,very_high]
    def __and__(a, b):
        return min(a,b)
    def __or__(a, b):
        return max(a,b)
    player=score(p)
    opp=score2(o)
    pLow=player[0]
    pMed=player[1]
    pHigh=player[2]
    pVHigh=player[3]
    oLow=opp[0]
    oMed=opp[1]
    oHigh=opp[2]
    oVHigh=opp[3]
    cLow=roundScore(c)[0]
    cMed=roundScore(c)[1]
    cHigh=roundScore(c)[2]
    cVHigh=roundScore(c)[3]
    roll=max([(pLow and (oMed))and(cLow or cMed or cHigh),
             (pMed and oHigh) and (cLow or cMed or cHigh),
             (pMed and (oMed))and(cLow or cMed),
             (pMed and (oLow))and(cLow or cMed),
             (pLow and oLow)and(cLow or cMed or cHigh),
             (oVHigh) and (pLow) and (cLow or cMed or cHigh),
             (oVHigh) and (pMed) and (cLow or cMed or cHigh),
             (oVHigh) and (pHigh) and (cLow or cMed or cHigh or cVHigh),
             (pHigh) and (oHigh)and(cLow or cMed),
             (pVHigh) and (oHigh)and(cLow or cMed),
             (pHigh) and (oLow or oMed)and(cLow),
             (pVHigh) and (oLow or oMed)and(cLow),
             (pMed) and (oVHigh) and (cLow or cMed or cHigh or cVHigh),
             (pLow) and (oVHigh) and (cLow or cMed or cHigh),
             (pLow) and (oHigh) and (cLow or cMed or cHigh or cVHigh),
             (oVHigh) and (pVHigh) and (cLow or cMed),
             ])
    if p+c>=100:
        return 0
    if roll>0.05:
        return 1
    else:
        return 0
