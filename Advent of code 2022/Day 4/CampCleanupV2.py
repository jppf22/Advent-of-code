import re

with open("Advent of code 2022/Day 4/input.txt",'r') as f:
    pairs = f.readlines()

res = 0
for pair in pairs:
    limts = list(map(int, re.findall("[0-9]+",pair)))
    
    if(range(max(limts[0],limts[2]),min(limts[1],limts[3])+1)):
        res += 1

print(res)
    
    
    