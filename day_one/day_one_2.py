with open('day1.csv', 'r') as fil:
    report = [line.rstrip('\n') for line in fil]

report = [int(i) for i in report]

for x in report:
    for y in report:
        if 2020-x-y in report:
            print(x,y,(x*y*(2020-x-y)))
    
