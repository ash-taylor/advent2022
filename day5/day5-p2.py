import re

with open ('input.txt', 'r') as f:
    lines = f.read().splitlines()

stackCount = 0

stack = [[] for _ in range(1, len(lines[0]), 4)]
        
for line in lines: 
    if line[1].isnumeric():  
        break
    
    stackCount = 0
    for i in range(1, len(line), 4): 
        if line[i].isalpha():
            stack[stackCount].append(line[i])
        stackCount += 1

for i in range(len(stack)):  
    stack[i].reverse()

with open ('instructions.txt', 'r') as f:
    rows = f.read().splitlines()

tempList = []

for row in rows:
    rowNumbers = re.findall("\d+",row)

    for i in range(int(rowNumbers[0])): 
        x = stack[int(rowNumbers[1]) - 1].pop()
        tempList.append(x)
    
    tempList.reverse()
    stack[int(rowNumbers[2]) - 1].extend(tempList) 
    tempList.clear()    

print("Part Two: ", end = "")
for i in range(len(stack)):
    print(f"{stack[i][len(stack[i]) - 1]}", end = "")
print()
