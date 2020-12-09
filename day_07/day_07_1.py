#How many bag colors can eventually contain at least one shiny gold bag?

file = open("day_07/input_07.csv", "r")

bags = []

for line in file.readlines():
    data = line.replace('bags', '').replace('bag', '').replace(' contain ', ', ').replace('other', '').replace('.', '').replace(' \n', '').split(' , ')

    for i in range(1, len(data)):
        if 'no' in data[i]:
            data[i] = []
        else:
            data[i] = [data[i][0], data[i][2:]]

    bags.append(data)

goal = ['shiny gold']
count = 0


def search(goal, count):
    for i in goal:
        for bag in bags:
            if any(i in bags_sort for bags_sort in bag[1:]) and bag[0] not in goal:
                goal.append(bag[0])
                count += 1

    return count

print("Number of Bags: ", search(goal, count))
