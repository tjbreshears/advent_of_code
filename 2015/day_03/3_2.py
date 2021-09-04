#How many houses receive at least one present?
#https://adventofcode.com/2015/day/3

with open('inputs/2015/day_03.csv') as f:
    data_raw = f.read()
    data = [char for char in data_raw]

data_santa = data[::2]
data_robot = data[1::2]

position_santa = [0,0]
position_robot = [0,0]
visited_santa = []
visited_robot = []
visited = []

def directions_santa ():
    for i in range(len(data_santa)):
        if data_santa[i] == '^':
            position_santa[1] += 1
        elif data_santa[i] == 'v':
            position_santa[1] -= 1
        elif data_santa[i] == '>':
            position_santa[0] += 1
        elif data_santa[i] == '<':
            position_santa[0] -= 1

        if str(position_santa) not in visited_santa:
            visited_santa.append(str(position_santa))

def directions_robot ():
    for i in range(len(data_robot)):
        if data_robot[i] == '^':
            position_robot[1] += 1
        elif data_robot[i] == 'v':
            position_robot[1] -= 1
        elif data_robot[i] == '>':
            position_robot[0] += 1
        elif data_robot[i] == '<':
            position_robot[0] -= 1

        if str(position_robot) not in visited_robot:
            visited_robot.append(str(position_robot))

def directions ():
    directions_santa()
    directions_robot()
    for i in visited_santa:
        visited.append(i)
    for i in visited_robot:
        if i not in visited:
            visited.append(i)
            
directions()
print(f'Unique Houses Visited: {len(visited)}')
