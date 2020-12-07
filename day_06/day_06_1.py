#For each group, count the number of questions to which anyone answered "yes".
#What is the sum of those counts?

with open('day_06/input_06.csv') as file:
    data = file.read().strip().split("\n\n")
    data = [i.replace("\n", "") for i in data]

groups = []
total = 0

for x in data:
    unique = len(set(x))
    groups.append(unique)

for num in range(0, len(groups)):
    total += groups[num]

print("Total Count: " + str(total))
