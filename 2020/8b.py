def execute(instruction_stack):
 #print(instruction_stack)
    instruction_pointer = 0
    accumulator = 0
    instruction_marked = set()
 
    while instruction_pointer not in instruction_marked and instruction_pointer < len(instruction_stack):
        #print(instruction_pointer)
        delta = 1
        (instruction, value) = instruction_stack[instruction_pointer]
        #print(i, inst, val)
        if instruction == "acc":
            accumulator += value
        elif instruction == "jmp":
            delta = value
        instruction_marked.add(instruction_pointer)
        instruction_pointer += delta

    return (instruction_pointer, accumulator)

def main(filein):
    lines = open(filein, 'r').read().split("\n")
    instruction_stack = [(instruction.split()[0], int(instruction.split()[1])) for instruction in lines]
    for i in range(len(instruction_stack)):
        instruction = instruction_stack[i][0]
        if instruction == "jmp" or instruction == "nop":
            instruction_stack[i] = ("nop" if instruction == "jmp" else "nop", instruction_stack[i][1])
            (ip, acc) = execute(instruction_stack)
            if ip >= len(instruction_stack):
                print(acc)
            instruction_stack[i] = (instruction, instruction_stack[i][1])

    #print(instruction_stack)

main("8.lk.in")