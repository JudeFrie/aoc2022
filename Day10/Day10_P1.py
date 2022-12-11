x = 1
cycles = 0
signal_strength = 0
signal_strengths_sum = 0

with open('AdventOfCodeDay10.txt', 'r') as file:
    data = file.read().split('\n')


def noop():
    global x
    global cycles
    global signal_strength
    global signal_strengths_sum
    cycles += 1
    signal_strength = cycles * x
    if cycles % 40 == 20 and cycles < 221:
        print(signal_strength)
        signal_strengths_sum += signal_strength


def addx(V):
    global x
    global cycles
    global signal_strength
    global signal_strengths_sum
    for i in range(2):
        cycles += 1
        signal_strength = cycles * x
        if cycles % 40 == 20 and cycles < 221:
            print(signal_strength)
            signal_strengths_sum += signal_strength
    x += int(V)


for i in range(len(data)):
    if data[i][:4] == 'addx':
        addx(data[i][5:])
    if data[i][:4] == 'noop':
        noop()
