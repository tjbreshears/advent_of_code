#What do you get if you multiply together the number of trees encountered on each of the listed slopes?

with open('day_three/day_three.csv') as file:
    path = [line.rstrip('\n') for line in file]

elevation = len(path)
down = 0
right = 0
count = 0

def toboggan (r,d):
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
    print (str(count))

toboggan(1,1)
toboggan(3,1)
toboggan(5,1)
toboggan(7,1)
toboggan(1,2)
