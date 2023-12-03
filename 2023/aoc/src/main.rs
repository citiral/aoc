use std::fs;

mod day1;
mod day2;
mod day3;

fn main() {
    let contents = fs::read_to_string("input/day3.txt").expect("Cannot find day3.txt");
    day3::part2(contents.as_str());
}
