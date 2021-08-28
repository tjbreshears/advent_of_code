#What value is in the accumulator?

instructions = []
accumulator = 0

with open('day_08/input_08.csv') as file:
    data = file.read().strip().split("\n")
    data = [i.replace("+", "") for i in data]

for i in data:
    instructions.append([i.split(" ")[0], int(i.split(" ")[1])])

start = 0
used =[]

def gameboy(line_run):
    global accumulator

    if line_run in used:
        print(accumulator)
    else:
        if instructions[line_run][0] == "nop":
            used.append(line_run)
            gameboy(line_run + 1)

        elif instructions[line_run][0] == "acc":
            used.append(line_run)
            accumulator += instructions[line_run][1]
            gameboy(line_run + 1)

        elif instructions[line_run][0] == "jmp":
            used.append(line_run)
            gameboy(line_run + instructions[line_run][1])

gameboy(start)
