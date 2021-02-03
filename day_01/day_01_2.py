#What is the product of the three entries that sum to 2020?
#https://adventofcode.com/2020/day/1

with open('day_01/input_01.csv', 'r') as file:
    report = [line.rstrip('\n') for line in file]

report = [int(i) for i in report]
solution = []

for x in report:
    for y in report:
        if 2020-x-y in report:
           if x not in solution:
                solution.append(x)
                
print("Numbers that add to 2,020: " + "{:,}".format(solution[0]) + ", " + "{:,}".format(solution[1]) + ", and " + "{:,}".format(solution[2]))
print("Product: " + "{:,}".format(solution[0]*solution[1]*solution[2]))
