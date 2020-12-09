#How many individual bags are required inside your single shiny gold bag?

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

def search(current_bag):

    count = 0
    children = []

    for bag in bags:
        if current_bag == bag[0]:
            children = [x for x in bag[1:]]

    for child in children:
        if child:
            count += int(child[0]) + int(child[0]) * search(child[1])

    return count

print("Number of Bags: ", search('shiny gold'))
