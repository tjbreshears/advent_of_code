#What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
#Thanks be to Kevin...again

import functools

with open('day_10/input_10.csv') as file:
    data = file.read().strip().split("\n")

chargers = [int(x) for x in data]
chargers.append(0)
chargers.append(max(chargers)+3)

difference = (1,2,3)

@functools.lru_cache  #Pure magic
def plugging(number):
    if number == max(chargers):
        return 1
    count = 0
    for dif in difference:
        if (number + dif) in chargers:
            count += plugging(number + dif)
    return count

print(plugging(0))
