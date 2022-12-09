scenic_score = 0
scenic_score_max = 0
with open("AdventOfCodeDay08.txt", 'r') as file:
    data = file.read().split('\n')

print(data)
length_y = len(data)
length_x = len(data[0])

tree_total = length_x * length_y


def vis_to_left(tree_y, tree_x):
    trees_vis = 0
    tree_value = data[tree_y][tree_x]
    for i in range(tree_x):
        if data[tree_y][i] >= tree_value:
            trees_vis = 1
        else:
            trees_vis += 1
    return trees_vis


def vis_to_right(tree_y, tree_x):
    trees_vis = 0
    tree_value = data[tree_y][tree_x]
    for i in range(length_x-1, tree_x, -1):
        if data[tree_y][i] >= tree_value:
            trees_vis = 1
        else:
            trees_vis += 1
    return trees_vis


def vis_to_top(tree_y, tree_x):
    trees_vis = 0
    tree_value = data[tree_y][tree_x]
    for i in range(tree_y):
        if data[i][tree_x] >= tree_value:
            trees_vis = 1
        else:
            trees_vis += 1
    return trees_vis


def vis_to_bottom(tree_y, tree_x):
    trees_vis = 0
    tree_value = data[tree_y][tree_x]
    for i in range(length_y-1, tree_y, -1):
        if data[i][tree_x] >= tree_value:
            trees_vis = 1
        else:
            trees_vis += 1
    return trees_vis


for i in range(length_x):
    for j in range(length_y):
        scenic_score = vis_to_left(i, j) * vis_to_right(i, j) * vis_to_top(i, j) * vis_to_bottom(i, j)
        if scenic_score > scenic_score_max:
            scenic_score_max = scenic_score

print(scenic_score_max)



