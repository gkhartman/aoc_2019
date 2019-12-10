/*  AOC Day 2: Intcode program interpreter
 *  Process and input Intcode program consisting of comma separated integers. Ex. 1,0,0,3,99.
 *  Programs are read left to right where the first integer (position 0) is the opcode.
 *  Opcodes:
 *    99: HALT
 *    1:  ADD <read_index1> <read_index2> <write_index>
 *    2:  MULT <read_index1> <read_index2> <write_index>
 *
 *  Each instruction is 4 positions wide.
 *
 *  Part1: Consume the puzzle input and replace instruction index 1 with the value 12 and
 *    instruction index 2 with value 2.After running from this state what is the value in
 *    instruction index 0?
 */

fn load_input() {
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let mass_int: i32 = line.unwrap().parse::<i32>().unwrap();
        total += get_req_fule(mass_int);
    }
}

fn main() -> std::io::Result<()> {
    Ok(())
}
