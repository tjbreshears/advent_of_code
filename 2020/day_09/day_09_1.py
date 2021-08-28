#

with open('day_09/input_09.csv') as file:
    all_data = file.read().strip().split("\n")

all_data = [int(x) for x in all_data]

cypher = []
xmas_code = []

for i in range(0,25):
    cypher.append(all_data[i])

for i in range(25,len(all_data)):
    xmas_code.append(all_data[i])

def screen():
    for x in cypher:
        for y in cypher:
            if int(xmas_code[0])-int(x)-int(y) == 0:
                cypher.append(xmas_code[0])
                cypher.remove(cypher[0])
                xmas_code.remove(xmas_code[0])
                screen()
            else:
                print(xmas_code[0])

screen()
#Gives the right answer about 1000 times...but it gives the right answer
