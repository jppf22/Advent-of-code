with open("Advent of code 2022/Day 6/input.txt") as f:
    inpt = f.read()

diff = int(input("How many characters are in the start packet?"))

for i in range(diff-1,len(inpt)): #the position will be i+1
    text = inpt[i-(diff-1):i+1]
    isAlldiff = True

    for j in range(len(text)):
        if(text[j] in text[j+1:]):
            isAlldiff = False
            break
    
    if(isAlldiff):
        print("Position where the last ", diff, "are diff: ", i+1)
        break

    
