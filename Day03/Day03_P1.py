import string

sum = 0
first_compartments = []
second_compartments = []
alphas = list("!" + string.ascii_lowercase + string.ascii_uppercase)
common_characters = []

with open("AdventOfCodeDay03.txt", "r") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("\n", "")
    first_compartments.append(data[i][:int(len(data[i])/2)])
    second_compartments.append(data[i][int(len(data[i])/2):])

for i in range(len(data)):
    common_characters.append([value for value in first_compartments[i] if value in second_compartments[i]])

for i in range(len(common_characters)):
    sum = sum + alphas.index(common_characters[i][0])

print(sum)