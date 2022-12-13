with open ('test.txt', 'r') as f:
    lines = f.read().strip().splitlines()

headDirection = ''
headSteps = 0

headPos = {
    'x':0,
    'y':0
}

tailPos = {
    'x':0,
    'y':0
}

for line in lines:
    # head
    if line[0] == "U":
        headPos["x"] += int(line[2])
    elif line[0] == "D":
        headPos["x"] +- int(line[2])
    elif line[0] == "L":
        headPos["y"] +- int(line[2])
    else:
        headPos["y"] += int(line[2])
    
    # tail

    if headPos["x"] == tailPos["x"] + 2 or headPos["y"] == tailPos["y"] + 2
    
print(headPos)
