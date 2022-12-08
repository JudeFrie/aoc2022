sum = 0

elf_set_one_range_start = []
elf_set_one_range_end = []
elf_set_two_range_start = []
elf_set_two_range_end = []

with open("AdventOfCodeDay04.txt", 'r') as file:
    text = file.readlines()

# fill elf sets
for i in range(len(text)):
    text[i] = text[i].replace("\n", "")
    elf_set_one_range_start.append(text[i].split(",")[0].split("-")[0])
    elf_set_one_range_end.append(text[i].split(",")[0].split("-")[1])
    elf_set_two_range_start.append(text[i].split(",")[1].split("-")[0])
    elf_set_two_range_end.append(text[i].split(",")[1].split("-")[1])

for i in range(len(elf_set_one_range_start)):
    if (list(set(range(int(elf_set_one_range_start[i]),int(elf_set_one_range_end[i])+1)).intersection(range(int(elf_set_two_range_start[i]),int(elf_set_two_range_end[i])+1))) != []):
        sum = sum + 1

print(sum)


