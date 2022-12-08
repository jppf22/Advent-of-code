with open("Advent of code 2022/Day 8/input.txt") as f:
    lines = f.read().strip()
    lines = lines.split('\n')
    #print(lines)

board_width = len(lines[0])
board_heigth = len(lines)

lines = list(list(map(int, list(line))) for line in lines)
print(lines)

def isVisibleRow(pos):
    isVisible = True
    left = lines[row][:pos[1]]
    #print(left)
    if(all((x < lines[pos[0]][pos[1]]) for x in left)):
        return True
    right = lines[row][pos[1]+1:]
    #print(right)
    if(all((x < lines[pos[0]][pos[1]]) for x in right)):
        return True
    return False

def isVisibleColumn(pos):
    above = []
    row = 0
    
    while row != pos[0]:
        above.append(lines[row][pos[1]])
        row+=1
    #print(above)

    if(all((x < lines[pos[0]][pos[1]]) for x in above)):
        return True

    row += 1 #so we don't count the position we're in
    below = []
    while row != board_heigth:
        below.append(lines[row][pos[1]])
        row += 1
    #print(below)
    if(all((x < lines[pos[0]][pos[1]]) for x in below)):
        return True
    return False

count = 0
for row in range(len(lines)):
    for column in range(len(lines[0])):
        pos = (row,column)
        if(isVisibleRow(pos) or isVisibleColumn(pos)):
            count += 1

print(count)