#For each group, count the number of questions to which everyone answered "yes".
#What is the sum of those counts?
#Thanks be to Kevin for huge help on this code.

answers = []

with open('day_06/input_06.csv') as file:
    data = file.read().strip().split("\n\n")

for i in data:
    answers.append(i.splitlines())

counts =[]

def checker(g):
	unanimous = list(g[0])
	for letters in g:
		for letter in g[0]:
			if letter not in letters:
				try:
					unanimous.remove(letter)
				except ValueError:
					pass
	counts.append(len(unanimous))

for group in answers:
	checker(group)

print("Total Count: " + str(sum(counts)))
