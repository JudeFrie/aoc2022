import copy

positions = [[1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000], [1000, 1000],
             [1000, 1000], [1000, 1000], [1000, 1000]]

arena_length = []
arenas = [[], [], [], [], [], [], [], [], [], []]
tail_history_sum = 0

with open("AdventOfCodeDay09.txt", 'r') as file:
    data = file.read().split('\n')

# create an arenas for each rope segment and place all segments in centre of respective arena
for i in range(2001):
    arena_length.append('.')
for i in range(2001):
    arenas[0].append(list(arena_length))
for i in range(len(arenas)):
    arenas[i] = copy.deepcopy(arenas[0])
    arenas[i][positions[0][0]][positions[0][1]] = i


# Functions for moving once
def move_tails():
    for i in range(1, 10):
        if ((positions[i][0]) == (positions[i-1][0]+2)) and ((positions[i][1]) != (positions[i-1][1]+2)) and ((positions[i][1]) != (positions[i-1][1]-2)):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][0] -= 1
            positions[i][1] = positions[i-1][1]
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][0]) == (positions[i-1][0]+1) and (positions[i][1] == (positions[i-1][1]+2))) or ((positions[i][0]) == (positions[i-1][0]+2) and (positions[i][1] == (positions[i-1][1]+2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][0] -= 1
            positions[i][1] -= 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][0]) == (positions[i-1][0]+1) and (positions[i][1] == (positions[i-1][1]-2))) or ((positions[i][0]) == (positions[i-1][0]+2) and (positions[i][1] == (positions[i-1][1]-2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][0] -= 1
            positions[i][1] += 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][0]) == (positions[i-1][0]-2)) and ((positions[i][1]) != (positions[i-1][1]+2)) and ((positions[i][1]) != (positions[i-1][1]-2)):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][0] += 1
            positions[i][1] = positions[i-1][1]
            arenas[i][positions[i][0]][positions[i][1]] = i
        if (((positions[i][0]) == (positions[i-1][0]-1)) and (positions[i][1] == (positions[i-1][1]+2))) or (((positions[i][0]) == (positions[i-1][0]-2)) and (positions[i][1] == (positions[i-1][1]+2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][0] += 1
            positions[i][1] -= 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if (((positions[i][0]) == (positions[i-1][0]-1)) and (positions[i][1] == (positions[i-1][1]-2))) or (((positions[i][0]) == (positions[i-1][0]-2)) and (positions[i][1] == (positions[i-1][1]-2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][0] += 1
            positions[i][1] += 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][1]) == (positions[i-1][1]+2)) and ((positions[i][0]) != (positions[i-1][0]+2)) and ((positions[i][0]) != (positions[i-1][0]-2)):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][1] -= 1
            positions[i][0] = positions[i-1][0]
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][1]) == (positions[i-1][1]+1) and ((positions[i][0]) == (positions[i-1][0]-2))) or ((positions[i][1]) == (positions[i-1][1]+2) and ((positions[i][0]) == (positions[i-1][0]-2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][1] -= 1
            positions[i][0] += 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if (((positions[i][1]) == (positions[i-1][1]+1)) and ((positions[i][0]) == (positions[i-1][0]+2))) or ((positions[i][1]) == (positions[i-1][1]+2) and (positions[i][0]) == ((positions[i-1][0]+2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][1] -= 1
            positions[i][0] -= 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][1]) == (positions[i-1][1]-2)) and ((positions[i][0]) != (positions[i-1][0]+2)) and ((positions[i][0]) != (positions[i-1][0]-2)):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][1] += 1
            positions[i][0] = positions[i-1][0]
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][1]) == (positions[i-1][1]-1) and ((positions[i][0]) == (positions[i-1][0]-2))) or ((positions[i][1]) == (positions[i-2][1]-2) and ((positions[i][0]) == (positions[i-1][0]-2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][1] += 1
            positions[i][0] += 1
            arenas[i][positions[i][0]][positions[i][1]] = i
        if ((positions[i][1]) == (positions[i-1][1]-1) and ((positions[i][0]) == (positions[i-1][0]+2))) or ((positions[i][1]) == (positions[i-1][1]-2) and ((positions[i][0]) == (positions[i-1][0]+2))):
            if i != 9:
                arenas[i][positions[i][0]][positions[i][1]] = '.'
            else:
                arenas[i][positions[i][0]][positions[i][1]] = '#'
            positions[i][1] += 1
            positions[i][0] -= 1
            arenas[i][positions[i][0]][positions[i][1]] = i


def move_right():
    arenas[0][positions[0][0]][positions[0][1]] = '.'
    positions[0][1] += 1
    arenas[0][positions[0][0]][positions[0][1]] = 0
    move_tails()


def move_left():
    arenas[0][positions[0][0]][positions[0][1]] = '.'
    positions[0][1] -= 1
    arenas[0][positions[0][0]][positions[0][1]] = 0
    move_tails()


def move_up():
    arenas[0][positions[0][0]][positions[0][1]] = '.'
    positions[0][0] += 1
    arenas[0][positions[0][0]][positions[0][1]] = 0
    move_tails()


def move_down():
    arenas[0][positions[0][0]][positions[0][1]] = '.'
    positions[0][0] -= 1
    arenas[0][positions[0][0]][positions[0][1]] = 0
    move_tails()


# run instructions through correct functions
for i in range(len(data)):
    if data[i][0] == 'U':
        for j in range(int(data[i][2:])):
            move_up()
    if data[i][0] == 'D':
        for j in range(int(data[i][2:])):
            move_down()
    if data[i][0] == 'L':
        for j in range(int(data[i][2:])):
            move_left()
    if data[i][0] == 'R':
        for j in range(int(data[i][2:])):
            move_right()

# create sum of tail history
for i in range(len(arenas[0])):
    for j in range(len(arenas[1])):
        if (arenas[9][i][j] == '#') or (arenas[9][i][j] == 9):
            tail_history_sum += 1

print(tail_history_sum)
