import string

sum = 0
first_elf = []
second_elf = []
third_elf = []
alphas = list("!" + string.ascii_lowercase + string.ascii_uppercase)
common_characters = []

with open("AdventOfCodeDay03.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("\n", "")
    if (i + 1) % 3 == 1:
        first_elf.append(data[i])
    if (i + 1) % 3 == 2:
        second_elf.append(data[i])
    if (i + 1) % 3 == 0:
        third_elf.append(data[i])

for i in range(len(first_elf)):
    common_characters.append([value for value in first_elf[i] if value in second_elf[i] and value in third_elf[i]])

print(common_characters)

for i in range(len(common_characters)):
    sum = sum + alphas.index(common_characters[i][0])

print(sum)
