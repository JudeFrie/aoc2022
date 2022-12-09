vis_tree_sum = 0

with open("AdventOfCodeDay08.txt", 'r') as file:
    data = file.read().split('\n')

print(data)
length_y = len(data)
length_x = len(data[0])

tree_total = length_x * length_y


def vis_from_left(tree_y, tree_x):
    tree_test = []
    tree_value = data[tree_y][tree_x]
    for i in range(tree_x):
        if data[tree_y][i] >= tree_value:
            tree_test.append('block')
    if 'block' not in tree_test:
        return 1
    else:
        return 0


def vis_from_right(tree_y, tree_x):
    tree_test = []
    tree_value = data[tree_y][tree_x]
    for i in range(tree_x+1,length_x):
        if data[tree_y][i] >= tree_value:
            tree_test.append('block')
    if 'block' not in tree_test:
        return 1
    else:
        return 0


def vis_from_top(tree_y, tree_x):
    tree_test = []
    tree_value = data[tree_y][tree_x]
    for i in range(tree_y):
        if data[i][tree_x] >= tree_value:
            tree_test.append('block')
    if 'block' not in tree_test:
        return 1
    else:
        return 0


def vis_from_bottom(tree_y, tree_x):
    tree_test = []
    tree_value = data[tree_y][tree_x]
    for i in range(tree_y+1, length_y):
        if data[i][tree_x] >= tree_value:
            tree_test.append('block')
    if 'block' not in tree_test:
        return 1
    else:
        return 0


for i in range(length_x):
    for j in range(length_y):
        if vis_from_left(i, j) + vis_from_right(i, j) + vis_from_top(i, j) + vis_from_bottom(i, j) == 0:
            vis_tree_sum += 1

print(tree_total - vis_tree_sum)



