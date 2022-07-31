mod binary_diagnostic;

fn main() {
    let input_data = binary_diagnostic::read_input_file("input");
    println!("Input:\n{:?}", input_data);

    for (i, column) in input_data.iter().enumerate() {
        println!("For col {}.\t MCB {}.\t LCB {}",
                 i,
                 binary_diagnostic::most_common_bit(column),
                 binary_diagnostic::least_common_bit(column)
        );
    }

    let gamma_rate = binary_diagnostic::gamma_rate(&input_data);
    let epsilon_rate = binary_diagnostic::epsilon_rate(&input_data);

    println!("Gamma rate: {}", gamma_rate);
    println!("Epsilon rate: {}", epsilon_rate);

    println!("Output: {}", gamma_rate*epsilon_rate);
}

