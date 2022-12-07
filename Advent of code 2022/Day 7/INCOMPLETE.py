
with open("Advent of code 2022/Day 7/input.txt") as f:
    lines = f.readlines()


def make_hash(lines):
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




test = make_hash(lines)
print(test)



