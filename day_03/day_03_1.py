#How many trees would you encounter?

with open('day_03/input_03.csv') as file:
    path = [line.rstrip('\n') for line in file]

elevation = len(path)
down = 0
right = 0
count = 0

while (down < elevation):
    if path[down][right] == "#":
        count += 1
    down += 1
    right += 3
    if right >= 30:
        right -= (len(path[down]))

print ("Trees Hit: " + str(count))
