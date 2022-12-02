
difAX = ord('X') - ord('A')

def getScoreRound(oponent, you):
    you = chr(ord(you)-difAX)
    
    score = ord(you) - ord('A') + 1 #value of the letter
    
    if(oponent == you):
        return score + 3
    elif((oponent == 'A' and you == 'C')
         or (oponent == 'B' and you == 'A')
         or (oponent == 'C' and you == 'B')):
         return score
    else:
        return score + 6

with open("Advent of code 2022/rockpaperscissors.txt",'r') as f:
    lines = f.readlines()

maxscore = 0

for line in lines:
    oponent = line[0]
    you = line[2]
    maxscore += getScoreRound(oponent,you)

print(maxscore)    
