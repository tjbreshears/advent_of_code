#How many total feet of ribbon should they order?
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

def ribbon ():
    global total
    for i in range(len(data)):
        peri = (data[i][0] * 2) + (data[i][1] * 2)
        bow = data[i][0] * data[i][1] * data[i][2]
        total += peri + bow
    print(f'Ribbon Needed: {total}')

ribbon()
