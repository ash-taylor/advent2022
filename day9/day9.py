with open ('input.txt', 'r') as f:
    lines = f.read().strip().splitlines()

headDirection = ''
headSteps = 0

headStart = {
    'x':0,
    'y':0
}

tailStart = {
    'x':0,
    'y':0
}

for line in lines:
    headDirection = line[0]
    print(headDirection)
    headSteps = line[2]
    print(headSteps)
