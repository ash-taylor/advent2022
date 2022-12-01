# imports helper functions to parse data from files
import aoc

# imports input as a list of strings, seperated by "\n"
lines = aoc.input_as_lines("part1.txt")

# init elf count, dict of calories and total calories
elf = 1
elves = {}
totalCalories = 0

# iterate through list
for line in lines:
    # if line is blank - add total cals value to elf in elves dict, then increment elf by 1 and reset total cals
    if line == '':
        elves[elf] = totalCalories
        elf += 1
        totalCalories = 0
    # if line isn't blank add value to total calories
    if line != '':
        totalCalories += int(line)

# returns largest value in elves dict - answers 'part 1'
mostCal = max(elves.values())

print(mostCal)

# creates a list of the values from above dict (total cals per elf)
values = []
for i in elves:
    values.append(elves[i])

# sorts the list of values from largest to smallest
values.sort(reverse=True)

# adds the top 3 largest values - answers 'part 2'
total = 0
for i in range(3):
    total += values[i]

print(total)