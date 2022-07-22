use std::fs;
use std::process::ExitCode;

#[derive(Debug)]
enum Operation {
    add_horizontal,
    add_aim,
}

#[derive(Debug)]
struct Instruction {
    operation: Operation,
    amount: i32,
}


fn main() {
    let instructions = read_input_file("input");
    println!("{:?}", instructions);

    let final_answer = simulate_position(instructions);
    println!("Final value: {:?}", final_answer);
}

/// Calculates the final position of the submarine.
fn simulate_position(instructions: Vec<Instruction>) -> i32 {
    let mut depth = 0;
    let mut horizontal = 0;
    let mut aim = 0;

    for instruction in instructions {
        match instruction.operation {
            Operation::add_aim => aim += instruction.amount,
            Operation::add_horizontal => {
                horizontal += instruction.amount;
                depth += instruction.amount * aim;
            }
        }
    }

    depth * horizontal
}

/// Parses a single instruction from the input file.
fn parse_instruction(input_string: &str) -> Instruction {
    let parts: Vec<&str> = input_string.split(' ').collect();
    let direction_str = parts[0];
    let amount: i32 = parts[1].parse().unwrap();

    match direction_str {
        "forward" => Instruction { operation: Operation::add_horizontal, amount },
        "up" => Instruction { operation: Operation::add_aim, amount: -amount },
        "down" => Instruction { operation: Operation::add_aim, amount },
        &_ => panic!()
    }
}

/// Reads the input file and returns the list of parsed instructions.
fn read_input_file(filename: &str) -> Vec<Instruction> {
    let contents = fs::read_to_string(filename)
        .expect("Reading input file failed");
    let mut output_instructions = Vec::new();

    let lines: Vec<&str> = contents.lines().collect();
    for line in lines {
        output_instructions.push(parse_instruction(line));
    }

    output_instructions
}