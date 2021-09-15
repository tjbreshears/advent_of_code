#How many strings are nice?
#https://adventofcode.com/2015/day/5

import re

with open('inputs/2015/day_05.csv') as file:
    input = file.read().strip().split("\n")
    input = [i.replace("\n", "") for i in data]

result = []
for word in input:
    if len(re.findall('[aeiou]', word)) > 2:
        if re.search(r'(\w)(\1)', word):
            if not re.search(r'ab|cd|pq|xy', word):
                result.append(word)

print(len(result))
