# What is the life support rating of the submarine?
# https://adventofcode.com/2021/day/3

with open('inputs/2021/day_03.csv', 'r') as f:
    data = [line.rstrip('\n') for line in f]

oxy_data = data
co2_data = data

oxy = []
co2 = []

for x in range(0,13):
    if len(oxy) == 1:
        oxy = int(oxy[0],2)
        break
    else:
        oxy = []
        most = []
        one = 0
        zero = 0
        for y in oxy_data:
            if y[x] == '0':
                zero += 1
            else:
                one += 1
        if one > zero:
            most.append('1')
        elif one < zero:
            most.append('0')
        elif one == zero:
            most.append('1')

        for y in oxy_data:
            if y[x] == most[0]:
                oxy.append(y)

        oxy_data = oxy

for x in range(0,13):
    if len(co2) == 1:
        co2 = int(co2[0],2)
        break
    else:
        co2 = []
        least = []
        one = 0
        zero = 0
        for y in co2_data:
            if y[x] == '0':
                zero += 1
            else:
                one += 1
        if one > zero:
            least.append('0')
        elif one < zero:
            least.append('1')
        elif one == zero:
            least.append('0')

        for y in co2_data:
            if y[x] == least[0]:
                co2.append(y)

        co2_data = co2

print(f'Oxygen Generation: {oxy}')
print(f'CO2 Scrubbing: {co2}')
print(f'Power Consumption: {oxy*co2}')
