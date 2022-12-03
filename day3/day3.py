import string

with open ('input.txt', 'r') as f:
    lines = f.read().splitlines()

points = {}

alphabet = string.ascii_letters

n = 1
for ch in alphabet:
    points[ch] = n
    n += 1

totalSum = 0

for line in lines:
    rucksack_1 = line[:len(line)//2]
    rucksack_2 = line[len(line)//2:]

    for ch in rucksack_1:
        if ch in rucksack_2:
            totalSum += points.get(ch)
            break

print(f"Part 1: {totalSum}")

# PART 2

for i in range(0, len(lines), 3):
    elf_1 = lines[i]
    elf_2 = lines[i+1]
    elf_3 = lines[i+2]

    for ch in elf_1:
        if ch in elf_2 and ch in elf_3:
            totalSum += points.get(ch)
            break

print(f"Part 2: {totalSum}")