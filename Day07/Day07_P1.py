directories_dic = {}
directories_dic_sums = {}
val = 0
sums_list = [0]*1000000
sum_in_directory = 0

with open("AdventOfCodeDay07.txt", 'r') as file:
    data = file.readlines()

# clean data
for i in range(len(data)):
    data[i] = data[i].replace('\n', '')

# make directories unique
for i in range(len(data)):
    j = i+1
    while j < (len(data)):
        if data[i][0:3] == 'dir':
            if data[i] == data[j]:
                data[j] = data[j].replace(" ", " dup")
        j += 1

for i in range(len(data)):
    j = i+1
    while j < (len(data)):
        if (data[i][2:4] == 'cd') and (data[i][5:] != '..'):
            if data[i] == data[j]:
                data[j] = data[j].replace("cd ", "cd dup")
        j += 1


# create dictionary of directories with directories as keys and sums as values initialized to zero
for i in range(len(data)):
    if (data[i][2:4] == 'cd') and (data[i][5:] != '..') and (data[i][5:] not in directories_dic_sums):
        directories_dic_sums[data[i][5:]] = 0


# create dictionary of directories with directories as keys and list of contents as values
for i in range(len(data)):
    if (data[i][2:4] == 'cd') and (data[i][5:] != '..'):
        directories_dic[data[i][5:]] = []
        j = i+1
        while data[j][0:4] != '$ cd':
            if data[j][0:4] != '$ ls':
                directories_dic[data[i][5:]].append(data[j])
            if j < len(data)-1:
                j += 1
            else:
                break


# iterative function that counts contents of directory
def sum_directory(directory):
    global sum_in_directory
    for i in range(len(directories_dic[directory])):
        if directories_dic[directory][i].split(" ")[0] != "dir":
            sum_in_directory += int(directories_dic[directory][i].split(" ")[0])
        else:
            sum_directory(directories_dic[directory][i].split(" ")[1])


# run sum_directory for each directory and create list of sums
for directory in directories_dic:
    sum_directory(directory)
    sums_list.append(sum_in_directory)
    sum_in_directory = 0

# keep sums that meet criteria and print sum of sums
for i in range(len(sums_list)):
    if sums_list[i] > 100000:
        sums_list[i] = 0
print(sum(sums_list))