# What do you get if you multiply your final horizontal position by your final
# depth?
# https://adventofcode.com/2021/day/2

with open('inputs/2021/day_02.csv', 'r') as f:
    data = [line.rstrip('\n') for line in f]

depth = 0
forward = 0
aim = 0

for x in data:
    if x[0] == 'u':
        aim -= int(x[-1])
    elif x[0] == 'd':
        aim += int(x[-1])
    elif x[0] == 'f':
        forward += int(x[-1])
        depth += aim * int(x[-1])

print(f'Depth x Forward: {depth*forward}')
