with open ('input.txt', 'r') as f:
    line = f.read()

stopLoop = False

for i in range(len(line)):
    duplicate = False
    for j in range(4):
        if line[i:i+4].count(line[i:i+4][j]) > 1:
            duplicate = True
            break
        if j == 3 and duplicate == False:
            print("Day 6: " + str(i+4))
            stopLoop = True
    if stopLoop:
        break
