#!/usr/bin/python3
# AOC Day 2: 1202 Program Alarm

# Opcode constants
ADD = 1
MULT = 2
HALT = 99

def is_valid_opcode(instr: int) -> bool:
    return int(instr) in [ADD, MULT, HALT]


def load_input(path='input.txt'):
    # Read input file, parse intcodes from csv and return intcode list.
    infile = open(path, 'r')
    intcode_str = infile.read()
    intcode_list = intcode_str.split(',')
    infile.close()
    for i in range(len(intcode_list)):
        intcode_list[i] = int(intcode_list[i])
    return intcode_list


def run(addr_1, addr_2, memory) -> int:
    # Initialize program counter to address 0.
    instr_ptr = 0

    memory[1] = addr_1
    memory[2] = addr_2

    while True:
        opcode_value = int(memory[instr_ptr])
        if is_valid_opcode(opcode_value):
            if opcode_value == HALT:
                # print('Loaded Instruction: HALT.')
                # print('Intcode position 0 value: {}'.format(memory[0]))
                return memory[0]
            if opcode_value == ADD:
                value1_idx = int(memory[instr_ptr + 1])
                value2_idx = int(memory[instr_ptr + 2])
                store_idx = int(memory[instr_ptr + 3])
                # print(f'Loaded Instruction: ADD {value1_idx} {value2_idx} {store_idx}.')
                memory[store_idx] = int(memory[value1_idx]) + int(memory[value2_idx])
            if opcode_value == MULT:
                value1_idx = int(memory[instr_ptr + 1])
                value2_idx = int(memory[instr_ptr + 2])
                store_idx = int(memory[instr_ptr + 3])
                # print(f'Loaded Instruction: MULT {value1_idx} {value2_idx} {store_idx}.')
                memory[store_idx] = int(memory[value1_idx]) * int(memory[value2_idx])

            instr_ptr += 4  # Increment program counter.
            # print(f'Program state: {memory}')

        else:
            print(f'ERROR: Bad Opcode Value: {opcode_value}.')


if __name__ == '__main__':

    init_memory_state = load_input()

    # Run Part 1 
    output = run(addr_1=12, addr_2=2, memory=init_memory_state[:])
    print(f'Part 1: {output}')

    # Run Part 2
    # Find which inputs (addresses 1 and 2) produce the output 19690720.
    iters = 0
    PART_2_OUTPUT = 19690720
    for input_1 in range(100):
        for input_2 in range(100):
            output = run(addr_1=input_1, addr_2=input_2, memory=init_memory_state[:])
            iters += 1
            if output == PART_2_OUTPUT:
                print('Part 2: {}'.format(100 * input_1 + input_2))
                print('Part 2 took {} iterations'.format(iters))
                exit()

