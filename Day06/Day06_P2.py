with open("AdventOfCodeDay06.txt", 'r') as file:
    text = file.read()

window = []
for i in range(14):
    window.append(text[i])
sum = 0


def window_test(window):
    sum_trues = 0
    for j in range(len(window)):
        for i in range(len(window)):
            if window[i] == window[j]:
                sum_trues = sum_trues + 1
    return sum_trues == 14


for line in text:
    sum = sum + 1
    if sum > 14:
        window.append(line)
        window.remove(window[0])
    if window_test(window):
        print(sum)