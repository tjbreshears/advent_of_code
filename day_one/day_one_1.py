with open('day1.csv', 'r') as fil:
    report = [line.rstrip('\n') for line in fil]

report = [int(x) for x in report]

for i in report:
    if 2020-i in report:
        print(i,2020-i,(i*(2020-i)))
    print(False)
