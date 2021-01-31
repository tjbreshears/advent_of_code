#Find the two entries that sum to 2020; what do you get if you multiply them together?

with open('day_01/input_01.csv', 'r') as file:
    report = [line.rstrip('\n') for line in file]

report = [int(x) for x in report]
solution = []

for i in report:
    if 2020-i in report:
        if i not in solution:
            solution.append(i)

print(f"Add to 2020: {solution[0]} and {solution[1]}")
print(f"Product: {solution[0]*solution[1]}")
