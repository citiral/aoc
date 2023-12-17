use std::{fs, env::args, error, process::exit};

mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;
mod day8;
mod day9;
mod day10;
mod day11;
mod day12;

macro_rules! d{
    ($d:ident) => {
        {
            (&$d::part1, &$d::part2)
        }
    };
}

fn main() {
    if let Some(day) = args().nth(1) {
        let path = format!("input/{day}.txt");
        let contents = fs::read_to_string(path.as_str()).expect(format!("Cannot find {path}").as_str());

        let implementations: (&dyn Fn(&str), &dyn Fn(&str)) = match day.as_str() {
            "day1" => d!(day1),
            "day2" => d!(day2),
            "day3" => d!(day3),
            "day4" => d!(day4),
            "day5" => d!(day5),
            "day6" => d!(day6),
            "day7" => d!(day7),
            "day8" => d!(day8),
            "day9" => d!(day9),
            "day10" => d!(day10),
            "day11" => d!(day11),
            "day12" => d!(day12),
            _ => {
                println!("Invalid day: '{day}'.");
                exit(1);
            }
        };

        implementations.0(contents.as_str());
        implementations.1(contents.as_str());

    } else {
        println!("Run with the day as argument");
    }
}
