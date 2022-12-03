
def getDuplicate(half1,half2):
    for x in half1:
        if(x in half2):
            return x

def getLetterPrio(letter):
    if('A' <= letter <= 'Z'):
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1


with open("Advent of code 2022/Day 3/input.txt",'r') as f:
    rucksacks = f.read()
    rucksacks = rucksacks.strip()
    #print(rucksacks)

rucksacks = rucksacks.split('\n')
#print(rucksacks)

res = 0
for sack in rucksacks:
    halves = (sack[:(len(sack)//2)],sack[(len(sack)//2):])
    #print(halves)
    duplicate = getDuplicate(halves[0],halves[1])
    res += getLetterPrio(duplicate)

print(res)



