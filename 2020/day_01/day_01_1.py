# Find the two entries that sum to 2020;
# what do you get if you multiply them together?
# https://adventofcode.com/2020/day/1

with open('inputs/2020/day_01.csv', 'r') as f:
    report = [line.rstrip('\n') for line in f]

report = [int(x) for x in report]
solution = []

for i in report:
    if 2020 - i in report:
        if i not in solution:
            solution.append(i)

print(f"Add to 2020: {solution[0]} and {solution[1]}")
print(f"Product: {solution[0]*solution[1]}")
