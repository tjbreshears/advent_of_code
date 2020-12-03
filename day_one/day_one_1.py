#Find the two entries that sum to 2020; what do you get if you multiply them together?

with open('day_one/day_one.csv', 'r') as file:
    report = [line.rstrip('\n') for line in file]

report = [int(x) for x in report]
solution = []

for i in report:
    if 2020-i in report:
        if i not in solution:
            solution.append(i)

print("Numbers that add to 2,020: " + "{:,}".format(solution[0]) + " and " + "{:,}".format(solution[1]))
print("Product: " + "{:,}".format(solution[0]*solution[1]))
