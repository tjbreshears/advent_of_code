#What is the ID of your seat?
#https://adventofcode.com/2020/day/5

with open('inputs/day_05.csv') as file:
    data = file.read().strip().split("\n")

IDlist = []

#Searches each letter in a boarding pass seat assignment
def boarding(ticket):
    row = range(0, 127)
    column = range(0, 7)

    for i in ticket:
        if i == "F":
            row = row[0:(len(row)) // 2]
        if i == "B":
            row = row[(len(row) + 1) // 2:]
        if i == "L":
            column = column[0:(len(column)) // 2]
        if i == "R":
            column = column[(len(column) + 1) // 2:]

#Calculates seat ID
    seat_ID = row.stop * 8 + column.stop
    IDlist.append(seat_ID)
    IDlist.sort()

#Looks at every boarding pass
def allSeats(data):
    for x in data:
        boarding(x)

#Find the missing seat
def finder():
    for y in range(len(IDlist)-1):
        if IDlist[y] + 1 != IDlist[y+1]:
            print(f"Missing Seat: {IDlist[y]+1}")
        else:
            pass

allSeats(data)
finder()
