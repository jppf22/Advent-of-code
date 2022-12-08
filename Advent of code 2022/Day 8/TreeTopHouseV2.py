with open("Advent of code 2022/Day 8/input.txt") as f:
    lines = f.read().strip()
    lines = lines.split('\n')
    #print(lines)

board_width = len(lines[0])
board_heigth = len(lines)

lines = list(list(map(int, list(line))) for line in lines)
print(lines)

def distanceHorizontal(pos): # returns the product of the horizontal distance
    tree_heigth = lines[pos[0]][pos[1]]

    def getDistance(side):
        if(len(side) == 0):
            return 0
        for tree in range(len(side)):
            if(side[tree] >= tree_heigth):
                return tree+1
        return len(side)

    isVisible = True
    left = lines[row][:pos[1]]
    left.reverse()
    right = lines[row][pos[1]+1:]
    return getDistance(left)*getDistance(right)



def distanceVertical(pos): # returns the product of the distance up and down
    tree_heigth = lines[pos[0]][pos[1]]

    def getDistance(side):
        if(not len(side)):
            return 0
        for tree in range(len(side)):
            if(side[tree] >= tree_heigth):
                return tree+1
        return len(side)

    above = []
    row = 0
    while row != pos[0]:
        above.append(lines[row][pos[1]])
        row+=1
    above.reverse()
    row += 1 #so we don't count the position we're in

    below = []
    while row != board_heigth:
        below.append(lines[row][pos[1]])
        row += 1

    return getDistance(below)*getDistance(above)

highest_distance = 0
for row in range(len(lines)):
    for column in range(len(lines[0])):
        pos = (row,column)
        #print(pos, distanceHorizontal(pos)*distanceVertical(pos))
        highest_distance = max(highest_distance, distanceHorizontal(pos)*distanceVertical(pos))
           
print(highest_distance)