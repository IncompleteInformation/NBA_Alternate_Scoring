def createScoreOrderList(pairList):
    whoJustScored = []
    prev = [0,0]
    for pair in pairList:
        if pair[0]!=prev[0]:
            whoJustScored.append("team1")
        elif pair[1]!=prev[1]:
            whoJustScored.append("team2")
        prev = pair

    return whoJustScored

def calculateBonusScores(orderList):
    t1Bonus,t2Bonus=0,0
    streak=1
    prev = None
    for e in orderList:
        if e==prev:
            if e=="team1":
                t1Bonus+=streak
            elif e=="team2":
                t2Bonus+=streak
            streak+=1
        else:
            streak=1
        prev = e

    return [t1Bonus,t2Bonus]

def calculate(pairList):
    scoreOrderList = createScoreOrderList(pairList)
    bonuses = calculateBonusScores(scoreOrderList)
    return bonuses
