with open ('input.txt', 'r') as f:
    lines = f.read().splitlines()

totalScore = 0

def round(line):
    if line == "A Y" or line == "B Z" or line == "C X":
        return 6
    elif line == "A X" or line == "B Y" or line == "C Z":
        return 3

def shapes(line):
    if line[2] == "X":
        return 1
    elif line[2] == "Y":
        return 2
    else:
        return 3

for line in lines:
    if not round(line):
        totalScore += shapes(line)
    else:
        totalScore += (round(line) + shapes(line))
        
print(f"Part One: {totalScore}\n")

totalScore = 0

def result(line, shape):
    global totalScore
    match shape:
        case "win":
            totalScore += 6
            if line[0] == "A":
                totalScore += 2
            elif line[0] == "B":
                totalScore += 3
            else:
                totalScore += 1
        case "draw":
            totalScore += 3
            if line[0] == "A":
                totalScore += 1
            elif line[0] == "B":
                totalScore += 2
            else:
                totalScore += 3
        case "lose":
            if line[0] == "A":
                totalScore += 3
            elif line[0] == "B":
                totalScore += 1
            else:
                totalScore += 2

for line in lines:
    if line [2] == "X":
        result(line, "lose")
    elif line[2] == "Y":
        result(line, "draw")
    else:
        result(line, "win")

print(f"Part Two: {totalScore}")