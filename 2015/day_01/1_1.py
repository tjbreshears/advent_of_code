# To what floor do the instructions take Santa?
# https://adventofcode.com/2015/day/1

with open("inputs/2015/day_01.csv") as f:
    data_raw = f.read()
    data = [char for char in data_raw]

counter = 0

for i in range(len(data)):
    if data[i] == '(':
        counter += 1
    elif data[i] == ')':
        counter -= 1

print(f'Final Floor: {counter}')
