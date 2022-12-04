with open ('input.txt', 'r') as f:
    lines = f.read().splitlines()

fullOverlap = 0

def areas(min, max):
    areaNumbers = set()
    for i in range(min, (max + 1)):
        areaNumbers.add(i)
    return areaNumbers


for line in lines:
    pair = line.split(",")

    elf_1 = pair[0].split("-")
    elf_2 = pair[1].split("-")

    difference_x = areas(int(elf_1[0]), int(elf_1[1])).difference(areas(int(elf_2[0]), int(elf_2[1])))
    difference_y = areas(int(elf_2[0]), int(elf_2[1])).difference(areas(int(elf_1[0]), int(elf_1[1])))

    if difference_x == set() or difference_y == set():
        fullOverlap += 1

print(f"Part one: {fullOverlap}")

overlap = 0

for line in lines:
    pair = line.split(",")

    elf_1 = pair[0].split("-")
    elf_2 = pair[1].split("-")

    difference_x = areas(int(elf_1[0]), int(elf_1[1])).difference(areas(int(elf_2[0]), int(elf_2[1])))
    difference_y = areas(int(elf_2[0]), int(elf_2[1])).difference(areas(int(elf_1[0]), int(elf_1[1])))

    if difference_x != areas(int(elf_1[0]), int(elf_1[1])) or difference_y != areas(int(elf_2[0]), int(elf_2[1])).difference(areas(int(elf_1[0]), int(elf_1[1]))):
        overlap += 1

print(f"Part Two: {overlap}")



# determine whether one pair fully contains the other. f

# If so - increase count by 1