#How many houses receive at least one present?
#https://adventofcode.com/2015/day/3

with open('inputs/2015/day_03.csv') as f:
    data_raw = f.read()
    data = [char for char in data_raw]

position = [0,0]
visited = []

def directions ():
    for i in range(len(data)):
        if data[i] == '^':
            position[1] += 1
        elif data[i] == 'v':
            position[1] -= 1
        elif data[i] == '>':
            position[0] += 1
        elif data[i] == '<':
            position [0] -= 1

        if str(position) not in visited:
            visited.append(str(position))

directions ()
print(f'Unique Houses Visited: {len(visited)}')
