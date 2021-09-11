# What is the position of the character that causes Santa to first enter the \
# basement?
# https://adventofcode.com/2015/day/1

with open('inputs/2015/day_01.csv') as f:
    data_raw = f.read()
    data = [char for char in data_raw]

counter = 0

for i in range(len(data)):
    if data[i] == '(':
        counter += 1
    elif data[i] == ')':
        counter -= 1
        if counter == -1:
            print(f'First Basement Encounter: {i+1}')
            break
