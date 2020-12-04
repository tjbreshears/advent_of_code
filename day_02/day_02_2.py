#How many passwords are valid according to the new interpretation of the policies?

import re

with open('day_02/input_02.csv') as file:
    passwords = [line.rstrip('\n') for line in file]

valid = 0

#regex
vLetter = '[a-z]'
vPosition1 = '^[0-9]{1,}'
vPosition2 = '\-[0-9]{1,}'
vPassword = '\:\s[a-z]{1,}'

for i in passwords:
    letter = re.search(vLetter, i).group(0)
    position1 = int(re.search(vPosition1, i).group(0)) - 1
    position2 = int(re.search(vPosition2, i).group(0)[1:]) - 1
    password = re.search(vPassword, i).group(0)[2:]

    if password[position1] == letter and password[position2] != letter:
        valid += 1
    elif password[position2] == letter and password[position1] != letter:
        valid += 1

print("Valid Passwords: " + str(valid))
