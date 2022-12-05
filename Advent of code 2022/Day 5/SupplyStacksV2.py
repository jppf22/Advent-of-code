import re

stacks = ["NDMQBPZ","CLZQMDHV","QHRDVFZG","HGDFN","NFQ","DQVZFBT","QMTZDVSH","MGFPNQ","BWRM"]
stacks = list(map(list, stacks)) 

with open("Advent of code 2022/Day 5/input.txt") as f:
    lines = f.readlines()

for line in lines:
    interpret = list(map(int, re.findall("[0-9]+",line)))
    # 0 - amount , 1 - start, 2 - finish

    amount = interpret[0]
    ini_pos = interpret[1] - 1
    end_pos = interpret[2] - 1

    stacks[end_pos].extend(stacks[ini_pos][len(stacks[ini_pos])-amount:])
    del(stacks[ini_pos][len(stacks[ini_pos])-amount:])

for stack in stacks:
    print(stack[len(stack)-1],end='')