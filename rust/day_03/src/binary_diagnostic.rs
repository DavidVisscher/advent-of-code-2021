use std::fs;

pub fn read_input_file(filename: &str) -> Vec<Vec<bool>> {
    let input_string = fs::read_to_string(filename)
        .expect("Reading input file failed");
    parse_input(input_string)
}

fn parse_input(input_string: String) -> Vec<Vec<bool>> {
    let lines : Vec<&str> = input_string.lines().collect();

    let mut columns = Vec::with_capacity(lines[0].len());

    for _ in 0..lines[0].len() {
        columns.push(Vec::with_capacity(lines.len()));
    }

    for line in lines {
        let parsed_line = parse_input_line(line);
        for (i, b) in parsed_line.iter().enumerate() {
            columns[i].push(*b)
        }
    }

    columns
}

fn parse_input_line(line_string: &str) -> Vec<bool> {
    let mut parsed_line: Vec<bool> = Vec::with_capacity(line_string.len());
    for char in line_string.chars(){
        match char {
            '0' => parsed_line.push(false),
            '1' => parsed_line.push(true),
            _ => panic!("Invalid character in input: {}", char)
        }
    }
    parsed_line
}


pub fn epsilon_rate(columns: &Vec<Vec<bool>>) -> i32 {
    let mut epsilon_chars: String = String::new();

    columns.iter().for_each(| column | {
        let mcb = least_common_bit(column);
        match mcb {
            true => epsilon_chars.push('1'),
            false => epsilon_chars.push('0')
        }
    });
    epsilon_chars = epsilon_chars.chars().collect();

    i32::from_str_radix(&epsilon_chars, 2).unwrap()
}

pub fn gamma_rate(columns: &Vec<Vec<bool>>) -> i32 {
    let mut gamma_digits: String = String::new();

    columns.iter().for_each(| column | {
        let mcb = most_common_bit(column);
        match mcb {
            true => gamma_digits.push('1'),
            false => gamma_digits.push('0')
        }
    });
    gamma_digits = gamma_digits.chars().collect();

    i32::from_str_radix(&gamma_digits, 2).unwrap()
}

pub fn most_common_bit(column: &[bool]) -> bool {
    let trues_falses = count_trues_falses(column);
    trues_falses[0] >= trues_falses[1]
}

pub fn least_common_bit(column: &[bool]) -> bool {
    let trues_falses = count_trues_falses(column);
    trues_falses[0] < trues_falses[1]
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic(expected = "Invalid character in input: 2")]
    fn test_parse_line() {
        assert_eq!(parse_input_line("0"), [false] );
        assert_eq!(parse_input_line("1"), [true]);
        assert_eq!(parse_input_line("101"), [true, false, true]);
        parse_input_line("0112001"); // Line that should cause the panic
    }

    #[test]
    fn test_parse_multiline() {
        assert_eq!(
            parse_input("01\n10\n11".to_string()),
            [
                [false, true, true],
                [true, false, true]
            ]
        );
    }

    #[test]
    fn test_gamma_rate() {
        {
            let input = parse_input("001".to_string());
            assert_eq!(gamma_rate(&input), 1);
        }
        {
            let input = parse_input("101\n111\n001".to_string());
            assert_eq!(gamma_rate(&input), 5);
        }
        {
            let input = parse_input("111\n111".to_string());
            assert_eq!(gamma_rate(&input), 7);
        }
    }

    #[test]
    fn test_epsilon_rate() {
        let input = parse_input("111\n110\n100".to_string());
        assert_eq!(epsilon_rate(&input), 1);
    }
}
