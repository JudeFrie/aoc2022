sum = 0

with open("AdventOfCodeDay02.txt", "r") as file:
    text = file.readlines()

for i in range(len(text)):
    text[i] = text[i].replace(" ", "")
    text[i] = text[i].replace("\n", "")
print(text)

for i in range(len(text)):
    if text[i][1] == 'X':
        sum = sum + 1
    if text[i][1] == 'Y':
        sum = sum + 2
    if text[i][1] == 'Z':
        sum = sum + 3
    if ((text[i][0] == 'A') and (text[i][1] == 'X')) or ((text[i][0] == 'B') and (text[i][1] == 'Y')) or ((text[i][0] == 'C') and (text[i][1] == 'Z')):
        sum = sum + 3
    if ((text[i][0] == 'A') and (text[i][1] == 'Y')) or ((text[i][0] == 'B') and (text[i][1] == 'Z')) or ((text[i][0] == 'C') and (text[i][1] == 'X')):
        sum = sum + 6
print(sum)
