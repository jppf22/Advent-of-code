

plays = ('A','B','C')




def getScoreRound(oponent, outcome):

    def getPlay(increment):
        result = ord(oponent) + increment
        if(chr(result) < 'A'):
            return 3
        elif(chr(result) > 'C'):
            return 1
        return result-ord('A')+1


    if(outcome == 'X'): #-1
        return getPlay(-1)
    elif(outcome == 'Y'): #0
        return 3 + getPlay(0)
    else: #+1
        return 6 + getPlay(1)

with open("Advent of code 2022/rockpaperscissors.txt",'r') as f:
    lines = f.readlines()

maxscore = 0

for line in lines:
    oponent = line[0]
    outcome = line[2]
    maxscore += getScoreRound(oponent,outcome)

print(maxscore)
   