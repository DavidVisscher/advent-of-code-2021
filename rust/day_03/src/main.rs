use std::fs;

fn main() {
    let input_data = read_input_file("input");
    println!("Input:\n{:?}", input_data);

    for (i, column) in input_data.iter().enumerate() {
        println!("For col {}.\t MCB {}.\t LCB {}",
                 i,
                 most_common_bit(column),
                 least_common_bit(column)
        );
    }

    let gamma_rate = gamma_rate(&input_data);
    let epsilon_rate = epsilon_rate(&input_data);

    println!("Gamma rate: {}", gamma_rate);
    println!("Epsilon rate: {}", epsilon_rate);

    println!("Output: {}", gamma_rate*epsilon_rate);
}


fn epsilon_rate(columns: &Vec<Vec<bool>>) -> i32 {
    let mut epsilon_chars: String = String::new();

    columns.iter().for_each(| column | {
        let mcb = least_common_bit(column);
        match mcb {
            true => epsilon_chars.push('1'),
            false => epsilon_chars.push('0')
        }
    });
    epsilon_chars = epsilon_chars.chars().rev().collect();

    i32::from_str_radix(&epsilon_chars, 2).unwrap()
}

fn gamma_rate(columns: &Vec<Vec<bool>>) -> i32 {
    let mut gamma_digits: String = String::new();

    columns.iter().for_each(| column | {
        let mcb = most_common_bit(column);
        match mcb {
            true => gamma_digits.push('1'),
            false => gamma_digits.push('0')
        }
    });
    gamma_digits = gamma_digits.chars().rev().collect();

    i32::from_str_radix(&gamma_digits, 2).unwrap()
}


fn count_trues_falses(column: &[bool]) -> [i32; 2] {
    let mut trues = 0;
    let mut falses = 0;

    column.iter().for_each(|bit| {
        match bit {
            true => trues += 1,
            false => falses += 1
        }
    });

    [trues, falses]
}

fn most_common_bit(column: &[bool]) -> bool {
    let trues_falses = count_trues_falses(column);
    trues_falses[0] >= trues_falses[1]
}

fn least_common_bit(column: &[bool]) -> bool {
    let trues_falses = count_trues_falses(column);
    trues_falses[0] < trues_falses[1]
}

fn read_input_file(filename: &str) -> Vec<Vec<bool>> {
    let file_contents = fs::read_to_string(filename)
        .expect("Reading input file failed");

    let lines : Vec<&str> = file_contents.lines().collect();

    let mut columns = Vec::with_capacity(lines[0].len());

    for _ in 0..lines[0].len() {
        columns.push(Vec::with_capacity(lines.len()));
    }

    for line in lines {
        for (i, char) in line.chars().enumerate() {
            match char {
                '0' => columns[i].push(false),
                '1' => columns[i].push(true),
                _ => panic!("Invalid character in input file {}", char)
            }
        }
    }
    columns
}