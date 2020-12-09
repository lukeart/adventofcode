def execute(instruction_stack):
    instruction_pointer = 0
    accumulator = 0
    instruction_marked = set()
 
    while instruction_pointer not in instruction_marked or instruction_pointer > len(instruction_stack):
        delta = 1
        (instruction, value) = instruction_stack[instruction_pointer]
        #print(i, inst, val)
        if instruction == "acc":
            accumulator += value
        elif instruction == "jmp":
            delta = value
        # elif inst == "nop":
        #     i += 0
        # else:
        #     print("unexpected instruction")
        instruction_marked.add(instruction_pointer)
        instruction_pointer += delta

    return (instruction_pointer, accumulator)

def main(filein):
    lines = open(filein, 'r').read().split("\n")
    instruction_stack = [(instruction.split()[0], int(instruction.split()[1])) for instruction in lines]
    (ip, acc) = execute(instruction_stack)
    #print(instruction_stack)
    print(acc)

main("8.lk.in")