sum = 0
calories_list = []

with open('AdventOfCodeDay01.txt', 'r') as file:
    text = file.readlines()

for line in text:
    if line == "\n":
        calories_list.append(sum)
        sum = 0
    else:
        sum = sum + int(line)

order = calories_list.sort()
answer = calories_list[-1]
print(answer)
