with open("AdventOfCodeDay06.txt", 'r') as file:
    text = file.read()

window = [text[0], text[1], text[2], text[3]]
sum = 0


def windowTest(window):
    return (window[0] != window[1]) and (window[0] != window[2]) and (window[0] != window[3]) and (window[1] != window[2]) and (window[1] != window[3]) and (window[2] != window[3])

for line in text:
    sum = sum + 1
    if sum > 4:
        window.append(line)
        window.remove(window[0])
    if windowTest(window):
        print(sum)


