def getCommon(group):
    for x in group[0]:
        if(x in group[1] and x in group[2]):
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
i = 0

while i < len(rucksacks):
    group = tuple(sack for sack in rucksacks[i:i+3])
    #print(group)
    common = getCommon(group)
    res += getLetterPrio(common)
    i += 3

print(res)