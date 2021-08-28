#In your batch file, how many passports are valid?
#https://adventofcode.com/2020/day/4

import re

with open('inputs/day_04.csv') as file:
    passports = file.read()
passw = re.split("\n\n", passports)

valid = 0
need = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for i in passw:
    if re.search(need[0], i) and \
    re.search(need[1], i) and \
    re.search(need[2], i) and \
    re.search(need[3], i) and \
    re.search(need[4], i) and \
    re.search(need[5], i) and \
    re.search(need[6], i):
        valid += 1

print(f"Valid Passports: {valid}")
