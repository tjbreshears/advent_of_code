#How many strings are nice?
#https://adventofcode.com/2015/day/5

#WORK IN PROGRESS

import re

with open('inputs/2015/day_05.csv') as f:
    data = f.read().split('\n')

vowels = ['a','e','i','o','u']
forbidden = ['ab','cd','pq','xy']
nice_vowel = []
nice = []

#vowel check
for i in data:
    counter = 0
    for char in i:
        if char in vowels:
            counter += 1
    if counter > 2:
        nice_vowel.append(i)

#double check
for i in nice_vowel:
    for index, character in enumerate(i[:-1]):
        if i[index + 1] == character:
            nice.append(i)


print(nice)
print(f'Nice strings: {len(nice)}')
