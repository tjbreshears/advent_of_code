# In the output values, how many times do digits 1, 4, 7, or 8 appear?
# https://adventofcode.com/2021/day/8

with open('inputs/2021/day_08.csv', 'r') as f:
    data =  f.read().strip().split("\n")
    data = [x.split('|') for x in data]

outputs = []
for x in range(len(data)):
    outputs.append(data[x][1])

outputs = [x.split(' ') for x in outputs]

counter = 0

for x in range(len(outputs)):
    for y in range(1,5):
        if len(outputs[x][y]) == 2 \
        or len(outputs[x][y]) == 4 \
        or len(outputs[x][y]) == 3 \
        or len(outputs[x][y]) == 7:
            counter += 1

print(f'Appearances of 1, 4, 7, and 8 in outputs: {counter}')
