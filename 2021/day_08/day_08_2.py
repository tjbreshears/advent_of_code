# What do you get if you add up all of the output values?
# https://adventofcode.com/2021/day/8

with open('inputs/2021/day_08.csv', 'r') as f:
    data =  f.read().strip().split("\n")
    data = [x.split('|') for x in data]

inputs = []
outputs = []

#split into inputs and outputs
for x in range(len(data)):
    outputs.append(data[x][1])
outputs = [x.split(' ') for x in outputs]
for x in range(len(data)):
    inputs.append(data[x][0])
inputs = [x.split(' ') for x in inputs]

#remove empty strings
for x in inputs:
    try:
        x.remove('')
    except ValueError:
        pass
for x in outputs:
    try:
        x.remove('')
    except ValueError:
        pass

#make all elements in alphabetical order. Not needed
for x in range(len(inputs)):
    for y in range(0,10):
        inputs[x][y] = ''.join(sorted(inputs[x][y]))
for x in range(len(outputs)):
    for y in range(0,4):
        outputs[x][y] = ''.join(sorted(outputs[x][y]))

values = []

for x in range(len(inputs)):
    value_one = []
    seven = []
    four = []
    one = []
    for y in range(0,10):
        if len(inputs[x][y]) == 3:
            seven = [char for char in inputs[x][y]]
        if len(inputs[x][y]) == 4:
            four = [char for char in inputs[x][y]]
        if len(inputs[x][y]) == 2:
            one = [char for char in inputs[x][y]]

    for z in range(0,4):
        if len(outputs[x][z]) == 7:
            value_one.append(8)
        elif len(outputs[x][z]) == 4:
            value_one.append(4)
        elif len(outputs[x][z]) == 3:
            value_one.append(7)
        elif len(outputs[x][z]) == 2:
            value_one.append(1)
        elif len(outputs[x][z]) == 5 and all(n in outputs[x][z] for n in seven):
            value_one.append(3)
        elif len(outputs[x][z]) == 6 and all(n in outputs[x][z] for n in seven) and all(m in outputs[x][z] for m in four):
            value_one.append(9)
        elif len(outputs[x][z]) == 6 and all(n in outputs[x][z] for n in seven) and len([ele for ele in outputs[x][z] if ele not in one]) == 4:
            value_one.append(0)
        elif len(outputs[x][z]) == 6 and len([ele for ele in outputs[x][z] if ele not in one]) == 5:
            value_one.append(6)
        elif len(outputs[x][z]) == 5 and len([ele for ele in outputs[x][z] if ele not in four]) == 2:
            value_one.append(5)
        elif len(outputs[x][z]) == 5 and len([ele for ele in outputs[x][z] if ele not in four]) == 3:
            value_one.append(2)
    values.append(value_one)
    values_one = []

#combine to make outputs one integer
value_combine = []
for x in range(len(values)):
    s = [str(i) for i in values[x]]
    res = int("".join(s))
    value_combine.append(res)

#sum nested list
def nested_sum(L):
    total = 0
    for i in L:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    print(f'Sum for output values: {total}')
nested_sum(value_combine)
