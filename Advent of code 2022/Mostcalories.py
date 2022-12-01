with open("input.txt", 'r') as f:
    lines = f.readlines()

elfs_calories = []
elfs_calories.append(0)

for line in lines:
    if line == '\n':
        elfs_calories.append(0)
    else:
        elfs_calories[-1] += int(line)

elfs_calories.sort(reverse=True)

# output for problem 1
print("The biggest number of calories is: ", elfs_calories[0]) 

# output for problem 2
print("The total of calories carried by the top 3 elves is: ", elfs_calories[0]+elfs_calories[1]+elfs_calories[2] )