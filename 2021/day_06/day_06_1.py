# How many lanternfish would there be after 80 days?
# https://adventofcode.com/2021/day/6

with open('inputs/2021/day_06.csv', 'r') as f:
    data =  f.read().strip().split(",")
    data = [int(x) for x in data]

day = 0

while day < 80:
    new = []
    for x in range(len(data)):
        if 1 <= data[x] <= 8:
            data[x] -= 1
        elif data[x] == 0:
            data[x] = 6
            new.append(8)
    data = data + new
    day += 1

print(f'Lanternfish after {day} days: {len(data)}')
