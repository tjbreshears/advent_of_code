#In your batch file, how many passports are valid?
#https://adventofcode.com/2020/day/4

import re

with open("day_04/input_04.csv", "r") as file:
    passportsRaw = file.read().strip().split("\n\n")
    passportsFormatted = [i.replace("\n", " ") for i in passportsRaw]

passportsPass = []
passports = []
valid = 0

counter = 0

for passport in passportsFormatted:
        if all( ["byr" in passport, \
        "iyr" in passport, \
        "eyr" in passport, \
        "hgt" in passport, \
        "hcl" in passport, \
        "ecl" in passport, \
        "pid" in passport] ):
            passportsPass.append(passport)

for passport in passportsPass:
    passports.append({})
    fields = re.findall("\w{3}\:#?\S*", passport)
    for i in fields:
        field = i.split(":")
        passports[counter][field[0]] = field[1]
    counter += 1

def hgtScan(h):
    if "cm" in h or "in" in h:
        unit = h[-2:]
        height = int(h[:-2])
        if unit == "cm" and 150 <= height <= 193:
            return True
        elif unit == "in" and 59 <= height <= 76:
            return True
        False

def scanner(passport):
	global valid

	# Check if ALL fields and then go and validate each one as a condition
	if (1920 <= int(passport["byr"]) <= 2002 and
        2010 <= int(passport["iyr"]) <= 2020 and
        2020 <= int(passport["eyr"]) <= 2030 and
        re.match("#[a-f0-9]{6}", passport["hcl"]) and
        re.match("(amb|blu|brn|gry|grn|hzl|oth)", passport["ecl"]) and
        re.fullmatch("\d{9}" , passport["pid"]) and
        hgtScan(passport["hgt"])):
            valid += 1

for i in passports:
    scanner(i)

print(f"Valid Passports: {valid}")
