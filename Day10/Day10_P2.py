x = 1
cycles = 0
crt = [[], [], [], [], [], []]
sprite = list('###.....................................')

for i in range(len(crt)):
    for j in range(40):
        crt[i].append('.')

with open('AdventOfCodeDay10.txt', 'r') as file:
    data = file.read().split('\n')


def sprite_update(x):
    global sprite
    for i in range(40):
        if i == x or i == x - 1 or i == x + 1:
            sprite[i] = '#'
        else:
            sprite[i] = '.'


def noop():
    global cycles
    if cycles < 40:
        if sprite[cycles] == '#':
            crt[0][cycles] = '#'
    if 40 <= cycles < 80:
        if sprite[cycles - 40] == '#':
            crt[1][cycles - 40] = '#'
    if 80 <= cycles < 120:
        if sprite[cycles - 80] == '#':
            crt[2][cycles - 80] = '#'
    if 120 <= cycles < 160:
        if sprite[cycles - 120] == '#':
            crt[3][cycles - 120] = '#'
    if 160 <= cycles < 200:
        if sprite[cycles - 160] == '#':
            crt[4][cycles - 160] = '#'
    if 200 <= cycles < 240:
        if sprite[cycles - 200] == '#':
            crt[5][cycles - 200] = '#'
    cycles += 1


def addx(V):
    global x
    global cycles
    for i in range(2):
        if cycles < 40:
            if sprite[cycles] == '#':
                crt[0][cycles] = '#'
        if 40 <= cycles < 80:
            if sprite[cycles - 40] == '#':
                crt[1][cycles - 40] = '#'
        if 80 <= cycles < 120:
            if sprite[cycles - 80] == '#':
                crt[2][cycles - 80] = '#'
        if 120 <= cycles < 160:
            if sprite[cycles - 120] == '#':
                crt[3][cycles - 120] = '#'
        if 160 <= cycles < 200:
            if sprite[cycles - 160] == '#':
                crt[4][cycles - 160] = '#'
        if 200 <= cycles < 240:
            if sprite[cycles - 200] == '#':
                crt[5][cycles - 200] = '#'
        cycles += 1
    x += int(V)
    sprite_update(x)


for i in range(len(data)):
    if data[i][:4] == 'addx':
        addx(data[i][5:])
    if data[i][:4] == 'noop':
        noop()

for i in range(len(crt)):
    print(crt[i])