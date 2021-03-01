#What is the highest seat ID on a boarding pass?
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

#Looks at every boarding pass
def allSeats(data):
    for x in data:
        boarding(x)

allSeats(data)
print(f"Highest Seat ID: {max(IDlist)}")
