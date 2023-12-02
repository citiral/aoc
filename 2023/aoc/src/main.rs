use std::fs;

mod day1;
mod day2;

fn main() {
    let contents = fs::read_to_string("input/day2.txt").expect("Cannot find day2.txt");
    day2::part2(contents.as_str());
}
