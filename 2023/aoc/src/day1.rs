pub fn part1(input: &str) {
    let mut sum = 0;
    for line in input.lines() {
        let mut digits: Vec<u32> = line.chars()
            .map(|x| x.to_digit(10))
            .filter(|x| x.is_some())
            .map(|x| x.unwrap())
            .collect();

        let val = digits.first().unwrap() * 10 + digits.last().unwrap();
        sum += val;
    }
    println!("{sum}");
}


pub fn part2(input: &str) {
    let mut sum = 0;
    for line in input.lines() {

        let mut first = -1;
        let mut last = -1;

        for i in 0..line.chars().count() {
            let c = line.chars().skip(i).next().unwrap();

            let val = if c.is_numeric() {
                c.to_digit(10).unwrap() as i32
            } else {
                if line[i..].starts_with("one") {
                    1
                } else if line[i..].starts_with("two") {
                    2
                } else if line[i..].starts_with("three") {
                    3
                } else if line[i..].starts_with("four") {
                    4
                } else if line[i..].starts_with("five") {
                    5
                } else if line[i..].starts_with("six") {
                    6
                } else if line[i..].starts_with("seven") {
                    7
                } else if line[i..].starts_with("eight") {
                    8
                } else if line[i..].starts_with("nine") {
                    9
                } else {
                    -1
                }
            };

            if val != -1 {
                if first == -1 {
                    first = val;
                }
                last = val;
            }
        }

        sum += first * 10 + last;
    }
    println!("{sum}");
}


#[test]
fn example() {
    part1("1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet");

    part2("two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen");
}