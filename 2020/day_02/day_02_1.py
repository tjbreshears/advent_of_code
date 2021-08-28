#How many passwords are valid according to their policies?
#https://adventofcode.com/2020/day/2

import re

with open('inputs/day_02.csv') as file:
    passwords = [line.rstrip('\n') for line in file]

valid = 0

#regex
vLetter = '[a-z]'
vMin = '^[0-9]{1,}'
vMax = '\-[0-9]{1,}'
vPassword = '\:\s[a-z]{1,}'

for i in passwords:
	letter = re.search(vLetter, i).group(0)
	min = int(re.search(vMin, i).group(0))
	max = int(re.search(vMax, i).group(0)[1:])
	password = re.search(vPassword, i).group(0)[2:]

	if min <= password.count(letter) <= max:
		valid += 1

print(f"Valid Passwords: {valid}")
