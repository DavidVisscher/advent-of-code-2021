use std::fs;

fn main() {
    let values = read_input_file("input");
    let sliding_window_values = sum_sliding_windows(values);
    let pairs = create_pairs(sliding_window_values);
    let increases = count_increases(pairs);
    println!("{:?}", increases)
}

/// Creates sums of sliding windows of three values
fn sum_sliding_windows(input_values: Vec<i32>) -> Vec<i32> {
    let mut output_values: Vec<i32> = Vec::new();
    for i in 0..(input_values.len()-2) {
        output_values.push(input_values[i] + input_values[i+1] + input_values[i+2])
    }
    output_values
}


/// Creates pairs from an input vector
fn create_pairs(input_values: Vec<i32>) -> Vec<[i32; 2]> {
    let mut output_pairs: Vec<[i32;2]> = Vec::with_capacity(input_values.len());

    for index in 0..(input_values.len()-1) {
        output_pairs.push(
            [input_values[index], input_values[index+1]]
        )
    }
    output_pairs
}

/// counts the amount of increasing pairs in the input vector.
fn count_increases(pairs: Vec<[i32; 2]>) -> i32 {
    let mut increases = 0;
    for pair in pairs {
        if pair[1] > pair[0] {
            increases += 1;
        }
    }
    increases
}

/// Reads the input file and parses each line into an i32
fn read_input_file(filename: &str) -> Vec<i32> {
    println!("Input filename {}", filename);
    let contents = fs::read_to_string(filename)
        .expect("Reading file failed.");

    let value_strings: Vec<&str> = contents.lines().collect();
    let mut values: Vec<i32> = Vec::with_capacity(value_strings.len());

    for value in value_strings {
        values.push(value.parse::<i32>().unwrap());
    }

    values
}
