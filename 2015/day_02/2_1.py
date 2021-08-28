#How many total square feet of wrapping paper should they order?
#https://adventofcode.com/2015/day/2

with open('inputs/2015/day_02.csv') as f:
    data_raw = f.read().split('\n')

data = []
total=0

for meas in data_raw:
    data.append(meas.split('x'))
data.pop(-1)

for x in range(len(data)):
    for y in range(3):
        data[x][y] = int(data[x][y])
    data[x].sort()

def wrap ():
    global total
    for i in range(len(data)):
        surface = (2 * data[i][0] * data[i][1]) + (2 * data[i][1] * data[i][2]) + (2 * data[i][0] * data[i][2])
        extra = data[i][0] * data[i][1]
        total += surface + extra
    print(f'Wrapping Paper Needed: {total}')

wrap()
