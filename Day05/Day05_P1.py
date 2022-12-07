import pandas as pd

stack_1 = ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V']
stack_2 = ['S', 'R', 'L', 'M', 'J', 'D', 'Q']
stack_3 = ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B']
stack_4 = ['R', 'S', 'C', 'L']
stack_5 = ['M', 'V', 'T', 'P', 'F', 'B']
stack_6 = ['T', 'R', 'Q', 'N', 'C']
stack_7 = ['G', 'V', 'R']
stack_8 = ['C', 'Z', 'S', 'P', 'D', 'L', 'R']
stack_9 = ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']

stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]
crate = ''
data = pd.read_excel('AdventOfCodeDay05.xlsx')
number_of_crates = 0
from_stack = 0
to_stack = 0


def pickup_crate(stack):
    global crate
    crate = stacks[stack][-1]
    stacks[stack] = stacks[stack][:-1]


def place_crate(stack):
    stacks[stack].append(crate)


def move_crates(number_of_crates, from_stack, to_stack):
    for i in range(number_of_crates):
        pickup_crate(from_stack-1)
        place_crate(to_stack-1)


def read_excel_line(line):
    global number_of_crates
    global from_stack
    global to_stack
    number_of_crates = data["boxes"][line]
    from_stack = data["from"][line]
    to_stack = data["to"][line]


for i in range(len(data)):
    read_excel_line(i)
    move_crates(number_of_crates, from_stack, to_stack)

answer = []
for i in range(len(stacks)):
    answer.append(stacks[i][-1])
print(answer)