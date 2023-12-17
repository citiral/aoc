use std::collections::{HashSet, HashMap};

fn get_next_value(values: &Vec<i64>) -> i64 {
    if values.iter().all(|v| *v == 0) {
        return 0;
    } else {
        let next_values: Vec<i64> = (0..values.len()-1).map(|i| values[i+1] - values[i]).collect();
        let last = values.last().unwrap();
        let next = get_next_value(&next_values);
        return last + next;
    }    
}

pub fn part1(input: &str) {
    let mut score = 0;

    for line in input.lines() {
        let values = line.split_whitespace().map(|v| v.parse::<i64>().unwrap()).collect();
        let next = get_next_value(&values);

        println!("next of [{line}] is {next}.");
        score += next;
    }

    println!("{score}");
}


pub fn part2(input: &str) {
    let mut score = 0;

    for line in input.lines() {
        let values = line.split_whitespace().map(|v| v.parse::<i64>().unwrap()).rev().collect();
        let next = get_next_value(&values);

        println!("next of [{line}] is {next}.");
        score += next;
    }

    println!("{score}");
}


#[test]
fn test() {
    part1("0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45");
    part2("0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45");
}