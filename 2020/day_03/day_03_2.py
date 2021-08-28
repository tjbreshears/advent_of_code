#What do you get if you multiply together the number of trees \
#encountered on each of the listed slopes?
#https://adventofcode.com/2020/day/3

with open('inputs/day_03.csv') as file:
    path = [line.rstrip('\n') for line in file]

#product for final answer
prod = 1

def toboggan (r,d):
    global prod
    elevation = len(path)
    down = 0
    right = 0
    count = 0

    while (down < elevation):
        if path[down][right] == "#":
            count += 1
        down += d
        right += r
        if right >= 30:
            right -= 31
    prod *= count
    print(f"Right: {r}, Down: {d}, Trees Hit: {count}")

toboggan(1,1)
toboggan(3,1)
toboggan(5,1)
toboggan(7,1)
toboggan(1,2)

print(f"Product: {prod}")
