# How many measurements are larger than the previous measurement?
# https://adventofcode.com/2021/day/1

with open('inputs/2021/day_01.csv', 'r') as f:
    data = [int(line.rstrip('\n')) for line in f]

increases = 0

for x in range(0,len(data)-1):
    if data[x] < data[x+1]:
        increases += 1

print(f'Number of times the measurements increase: {increases}')
