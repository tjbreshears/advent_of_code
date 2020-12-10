#What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

with open('day_10/input_10.csv') as file:
    data = file.read().strip().split("\n")

chargers = sorted(int(x) for x in data)
used = []

injolt = 0
ones = 0
twos = 0
threes = 0

def plugging ():
    global injolt, ones, twos, threes
    if len(chargers) == 0:
        print(ones, threes+1, ones*(threes+1))
    else:
        for charger in chargers:
            if charger - injolt == 1:
                ones += 1
                chargers.remove(charger)
                used.append(charger)
                injolt = charger
                plugging()
            if charger - injolt == 2:
                twos += 1
                injolt = charger
                chargers.remove(charger)
                used.append(charger)
                injolt = charger
                plugging()
            if charger - injolt == 3:
                threes += 1
                injolt = charger
                chargers.remove(charger)
                used.append(charger)
                injolt = charger
                plugging()

plugging()
print(chargers)
print(used)
