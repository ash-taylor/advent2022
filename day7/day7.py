class Node:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        prefix = (" " * self.get_level() * 2) + "|__" if self.parent else ""
        print(prefix + self.name + " (" + str(self.size) + ")")
        if self.children:
            for child in self.children:
                child.print_tree()

    def calculate_size(self):
        if self.children:
            for child in self.children:
                child.calculate_size()
        if self.parent:
            self.parent.size += self.size

partOne = 0
def part_one(self):
    global partOne
    if self.children:
        for child in self.children:
            part_one(child)
    if self.size < 100000 and self.name[0:6] == "folder":
        partOne += self.size

toDelete = 0
def part_two(self):
    global toDelete
    if self.name == "/":
        toDelete = self.size
    if self.children:
        for child in self.children:
            part_two(child)
    if self.name[0:6] == "folder" and self.size > (update_size - free_space):
        if self.size < toDelete:
            toDelete = self.size
            
        
root = Node("/")
curDir = root

with open ('input.txt', 'r') as f:
    lines = f.read().strip().splitlines()

for line in lines:
    command = line.split()
    if command[1] == "cd":
        if command[2] == "/":
            curDir = root
        elif command[2] == "..":
            if curDir.parent: 
                curDir = curDir.parent
        else:
            for child in curDir.children:
                if child.name == "folder_" + command[2]:
                    curDir = child
    elif command[1] == "ls":
        continue
    elif command[0] == "dir":
        subDir = Node("folder_" + command[1])
        subDir.size = 0
        curDir.add_child(subDir)
    else:
        item = Node("file_" + command[1])
        item.size = int(command[0])
        curDir.add_child(item)

root.calculate_size()
root.print_tree()
part_one(root)

print("Part One: " + str(partOne))

total_space = 70000000
update_size = 30000000
used_space = root.size
free_space = total_space - used_space

part_two(root)

print("Part Two: " + str(toDelete))