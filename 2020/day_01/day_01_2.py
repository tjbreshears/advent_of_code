#What is the product of the three entries that sum to 2020?
#https://adventofcode.com/2020/day/1

with open('inputs/day_01.csv', 'r') as f:
    report = [line.rstrip('\n') for line in f]

report = [int(i) for i in report]
solution = []

for x in report:
    for y in report:
        if 2020-x-y in report:
           if x not in solution:
                solution.append(x)

print(f"Numbers that add to 2020: {solution[0]}, {solution[1]}, and {solution[2]}")
print(f"Product: {solution[0]*solution[1]*solution[2]}")
