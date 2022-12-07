
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


res = 0
for str_level in dir_size:
    level_size = size_at_level(str_level)
    if(level_size <= 100000):
        res += level_size

print(res) 


        
        

























'''def make_hash(lines):
    root = {}
    sub_root = root

    for line in lines:
        if(line.startswith("$ cd ")):
            dir_name = line.removeprefix("$ cd ")

            if(dir_name == ".."):
                sub_root = sub_root[".."]
            else:
                dir = {"..": sub_root}
                sub_root[dir_name] = dir
        elif(line[0].isdigit()):
            size, name = line.split()
            sub_root[name] = int(size)
    return root
'''





