#In your batch file, how many passports are valid?

import re

with open('day_04/input_04.csv') as file:
    passports = file.read()

valid = 0
need = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passw = re.split("\n\n", passports)
print(passw)

for i in passw:
    if re.search(need[0], i) and re.search(need[1], i) and re.search(need[2], i) and re.search(need[3], i) and re.search(need[4], i) and re.search(need[5], i) and re.search(need[6], i):
        valid += 1

print(valid)
