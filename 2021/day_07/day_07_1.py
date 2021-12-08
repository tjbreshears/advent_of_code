# How much fuel must they spend to align to that position?
# https://adventofcode.com/2021/day/7

with open('inputs/2021/day_07.csv', 'r') as f:
    data =  f.read().strip().split(",")
    data = [int(x) for x in data]

best = 999999999
position = 0

while position < max(data):
    fuel = 0
    for x in data:
        fuel += abs(x-position)
    if fuel < best:
        best = fuel
    position += 1

print(f'Least amount of fuel used:{int(best)}')
