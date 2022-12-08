with open ('input.txt', 'r') as f:
    lines = f.read().strip().splitlines()


def part_one():
    treesVisible = (len(lines) * 2) + (len(lines[0]) * 2) - 4
    currentTree = 0
    Visible = False

    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if x != 0 and y != 0 and x != (len(lines)-1) and y != (len(lines[0])-1):

                visible = False
                currentTree = int(lines[x][y])

                for up in range(x-1, -1, -1):
                    compare = int(lines[up][y])
                    if compare >= currentTree:
                        visible = False
                        break
                    else:
                        visible = True

                if visible == False:
                    for left in range(y-1, -1, -1):
                        compare = int(lines[x][left])
                        if compare >= currentTree:
                            visible = False
                            break
                        else:
                            visible = True

                if visible == False:
                    for right in range(y+1, len(lines[0])):
                        compare = int(lines[x][right])
                        if compare >= currentTree:
                            visible = False
                            break
                        else:
                            visible = True

                if visible == False:
                    for down in range(x+1, len(lines)):
                        compare = int(lines[down][y])
                        if compare >= currentTree:
                            visible = False
                            break
                        else:
                            visible = True

                if visible == True:
                    treesVisible += 1

    print("Part One: " + str(treesVisible))


def part_two():
    currentTree = 0
    scenicScoreTotal = 0
        
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if x != 0 and y != 0 and x != (len(lines)-1) and y != (len(lines[0])-1):

                scenicScoreUp = 0
                scenicScoreLeft = 0
                scenicScoreRight = 0
                scenicScoreDown = 0

                currentTree = int(lines[x][y])

                for up in range(x-1, -1, -1):
                    compare = int(lines[up][y])
                    if compare >= currentTree:
                        scenicScoreUp += 1
                        break
                    else:
                        scenicScoreUp += 1

                for left in range(y-1, -1, -1):
                    compare = int(lines[x][left])
                    if compare >= currentTree:
                        scenicScoreLeft += 1
                        break
                    else:
                        scenicScoreLeft += 1

                for right in range(y+1, len(lines[0])):
                    compare = int(lines[x][right])
                    if compare >= currentTree:
                        scenicScoreRight += 1
                        break
                    else:
                        scenicScoreRight += 1

                for down in range(x+1, len(lines)):
                    compare = int(lines[down][y])
                    if compare >= currentTree:
                        scenicScoreDown += 1
                        break
                    else:
                        scenicScoreDown += 1

                if scenicScoreTotal < (scenicScoreUp * scenicScoreLeft * scenicScoreRight * scenicScoreDown):
                    scenicScoreTotal =  scenicScoreUp * scenicScoreLeft * scenicScoreRight * scenicScoreDown
    
    print("Part Two: " + str(scenicScoreTotal))


part_one()
               
part_two()