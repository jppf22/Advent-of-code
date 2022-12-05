import re

stacks = ["NDMQBPZ","CLZQMDHV","QHRDVFZG","HGDFN","NFQ","DQVZFBT","QMTZDVSH","MGFPNQ","BWRM"]
stacks = list(map(list, stacks)) 

with open("Advent of code 2022/Day 5/input.txt") as f:
    lines = f.readlines()

for line in lines:
    interpret = list(map(int, re.findall("[0-9]+",line)))
    # 0 - amount , 1 - start, 2 - finish

    i = interpret[0]
    while i > 0:
        unit = stacks[interpret[1]-1].pop()
        stacks[interpret[2]-1].append(unit)
        i -= 1

for stack in stacks:
    print(stack[len(stack)-1],end='')