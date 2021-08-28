#Find Santa the lowest positive number that produces such a hash. (6 zeros)
#https://adventofcode.com/2015/day/4

from hashlib import md5

with open('inputs/2015/day_04.txt') as f:
    input = f.read().replace('\n', '')

def hasher(key):
    for i in range(10000000):
        message = key + str(i)
        if md5(message.encode()).hexdigest()[:6] == '000000':
            print(i)
            break

hasher(input)
