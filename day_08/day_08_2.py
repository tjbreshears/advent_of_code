#What is the value of the accumulator after the program terminates?

instructions = []

with open('day_08/input_08.csv') as file:
    data = file.read().strip().split("\n")
    data = [i.replace("+", "") for i in data]

for i in data:
    instructions.append([i.split(" ")[0], int(i.split(" ")[1])])

accumulator = 0
start = 0
used =[]

def gameboy(line_run):
    global accumulator, used

    if line_run in used:
        pass
    elif line_run == len(instructions):
        print("Success!")
        print(f"Accumulator: {accumulator}")
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

for i in range(len(instructions)):
    if instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
        used = []
        accumulator = 0
        gameboy(0)
        instructions[i][0] = "jmp"
    elif instructions[i][0] == "nop":
        instructions[i][0] = "jmp"
        used = []
        accumulator = 0
        gameboy(0)
        instructions[i][0] = "nop"
