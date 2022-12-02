
difAX = ord('X') - ord('A')

def getScoreRound(oponent, you):
    you = chr(ord(you)-difAX)
    
    if(oponent == you):
        return 3
    elif((oponent == 'A' and you == 'C')
         or (oponent == 'B' and you == 'A')
         or (oponent == 'C' and you == 'B')):
         return 0
    else:
        return 6

with open("rockpaperscissors.txt",'r') as f:
    lines = f.readlines()

print(getScoreRound('A','A'))
