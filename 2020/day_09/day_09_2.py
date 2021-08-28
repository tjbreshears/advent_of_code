#What is the encryption weakness in your XMAS-encrypted list of numbers?

with open('day_09/input_09.csv') as file:
    all_data = file.read().strip().split("\n")

all_data = [int(x) for x in all_data]

def weakness ():
    for i in range(len(all_data)):
        counter = 0
        for e in range(i, len(all_data)):
            counter += all_data[e]
            if counter == 69316178:  #answer from part 1
                a = all_data[i:e+1]
                answer = min(a) + max(a)
                print(answer)

weakness()
# gives two answers...only the first one is right
