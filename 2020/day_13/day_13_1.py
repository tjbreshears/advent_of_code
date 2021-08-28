#What is the ID of the earliest bus you can take to the airport multiplied
#by the number of minutes you'll need to wait for that bus?
#https://adventofcode.com/2020/day/13

import math

raw_data = open("inputs/day_13.csv").read().split('\n')
raw_buses = raw_data[1].split(',')

time = int(raw_data[0])
buses = [int(entry) for entry in raw_buses if entry != 'x']
soonest = [0,1000000000] #set initial conditions to compare against

for bus in buses:
    close = math.ceil(time/bus)*bus
    if close < soonest[1]:
        soonest[1] = close
        soonest[0] = bus
    else:
        pass

wait = soonest[1]-time
answer = soonest[0]*wait

print(f"Bus ID: {soonest[0]}")
print(f"Minutes Waited: {wait}")
print(f"Product: {answer}")
