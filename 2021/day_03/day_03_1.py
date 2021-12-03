# What is the power consumption of the submarine?
# https://adventofcode.com/2021/day/3

with open('inputs/2021/day_03.csv', 'r') as f:
    data = [line.rstrip('\n') for line in f]

gamma = []
epsilon = []

for x in range(0,12):
    one = 0
    zero = 0
    for y in data:
        if y[x] == '0':
            zero += 1
        else:
            one += 1
    if one > zero:
        gamma.append('1')
    elif one < zero:
        gamma.append('0')

for x in range(0,12):
    one = 0
    zero = 0
    for y in data:
        if y[x] == '0':
            zero += 1
        else:
            one += 1
    if one < zero:
        epsilon.append('1')
    elif one > zero:
        epsilon.append('0')

gamma = int("".join(gamma),2)
epsilon = int("".join(epsilon),2)

print(f'Gamma: {gamma}')
print(f'Epsilon: {epsilon}')
print(f'Power Consumption: {gamma*epsilon}')
