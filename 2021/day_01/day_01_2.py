# How many sums are larger than the previous sum?
# https://adventofcode.com/2021/day/1

with open('inputs/2021/day_01.csv', 'r') as f:
    data = [int(line.rstrip('\n')) for line in f]

increases = 0

for x in range(0,len(data)-3):
    a = data[x]+data[x+1]+data[x+2]
    b = data[x+1]+data[x+2]+data[x+3]
    if a < b:
        increases += 1

print(f'Number of times the sums increase: {increases}')
