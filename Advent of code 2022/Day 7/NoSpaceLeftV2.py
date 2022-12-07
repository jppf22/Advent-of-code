
with open("Advent of code 2022/Day 7/input.txt") as f:
    inpt = f.read()
    inpt = inpt.split("$ ")


file_sys = {}
dir_size = {}
curr_level = []

for command in inpt[1:]:
    command = command[:-1].split('\n') #-1 so there isn't an empty space ['']

    if(len(command) == 1): # cd ------------------------
        command = command[0].split()
        if(command[1] == ".."):
            curr_level.pop()
        else:
            curr_level.append(command[1])
            file_sys['/'.join(curr_level)] = []
            
    else: # ls ---------------------
        str_level = '/'.join(curr_level)
        size = 0
        for child in command[1:]:
            first_ele = child.split()[0]
            if(first_ele == "dir"):
                file_sys[str_level].append(f'{str_level}/{child.split()[1]}')
            else:
                size += int(first_ele)
        
        dir_size[str_level] = size # the sum of all individual files (not counting children)


def size_at_level(str_level):
    size = dir_size[str_level]
    for child in file_sys[str_level]:
        size += size_at_level(child)
    return size

total_space = 70000000
free_space = total_space - size_at_level('/')
needed_space = 30000000 - free_space

smallest = 1e10
for level in dir_size:
    if(size_at_level(level) >= needed_space):
        smallest = min(smallest,size_at_level(level))

print(smallest)
