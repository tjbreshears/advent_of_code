# How many lanternfish would there be after 256 days?
# https://adventofcode.com/2021/day/6

with open('inputs/2021/day_06.csv', 'r') as f:
    data =  f.read().strip().split(",")
    data = [int(x) for x in data]

day = 0

freq = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for i in data:
    freq[i] = freq.get(i, 0) + 1


while day < 256:
    new = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for x in range(0,8):
        new[x] = freq[x+1]
    new[8] = freq[0]
    new[6] += freq[0]
    freq = new
    day += 1

print(f'Lanternfish after {day} days: {sum(freq.values())}')
