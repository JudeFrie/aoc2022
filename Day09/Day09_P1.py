import copy

tail_pos = [750, 750]
head_pos = [750, 750]
arena_length = []
arena_head = []
arena_tail = []
tail_history_sum = 0

with open("AdventOfCodeDay09.txt", 'r') as file:
    data = file.read().split('\n')

# create an arena for head and place head in centre. Create another arena for tail and place tail in centre
for i in range(1500):
    arena_length.append(0)
for i in range(1500):
    arena_head.append(list(arena_length))
arena_tail = copy.deepcopy(arena_head)
arena_head[head_pos[0]][head_pos[1]] = 'H'
arena_tail[tail_pos[0]][tail_pos[1]] = 'T'


# Functions for moving a single time
def move_up():
    arena_head[head_pos[0]][head_pos[1]] = 0
    head_pos[0] += 1
    arena_head[head_pos[0]][head_pos[1]] = 'H'
    if (tail_pos[0]) == (head_pos[0]-2):
        arena_tail[tail_pos[0]][tail_pos[1]] = '#'
        tail_pos[0] += 1
        tail_pos[1] = head_pos[1]
        arena_tail[tail_pos[0]][tail_pos[1]] = 'T'


def move_down():
    arena_head[head_pos[0]][head_pos[1]] = 0
    head_pos[0] -= 1
    arena_head[head_pos[0]][head_pos[1]] = 'H'
    if (tail_pos[0]) == (head_pos[0]+2):
        arena_tail[tail_pos[0]][tail_pos[1]] = '#'
        tail_pos[0] -= 1
        tail_pos[1] = head_pos[1]
        arena_tail[tail_pos[0]][tail_pos[1]] = 'T'


def move_left():
    arena_head[head_pos[0]][head_pos[1]] = 0
    head_pos[1] -= 1
    arena_head[head_pos[0]][head_pos[1]] = 'H'
    if (tail_pos[1]) == (head_pos[1]+2):
        arena_tail[tail_pos[0]][tail_pos[1]] = '#'
        tail_pos[1] -= 1
        tail_pos[0] = head_pos[0]
        arena_tail[tail_pos[0]][tail_pos[1]] = 'T'


def move_right():
    arena_head[head_pos[0]][head_pos[1]] = 0
    head_pos[1] += 1
    arena_head[head_pos[0]][head_pos[1]] = 'H'
    if (tail_pos[1]) == (head_pos[1]-2):
        arena_tail[tail_pos[0]][tail_pos[1]] = '#'
        tail_pos[1] += 1
        tail_pos[0] = head_pos[0]
        arena_tail[tail_pos[0]][tail_pos[1]] = 'T'


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
for i in range(len(arena_length)):
    for j in range(len(arena_length)):
        if (arena_tail[i][j] == '#') or (arena_tail[i][j] == 'T'):
            tail_history_sum += 1

print(tail_history_sum)