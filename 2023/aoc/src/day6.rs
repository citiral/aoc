pub fn part1(input: &str) {
    let mut score = 1;

    let mut lines = input.lines();

    let time = lines.next().unwrap().split_whitespace().skip(1).map(|t| t.parse::<u64>().unwrap());
    let dist = lines.next().unwrap().split_whitespace().skip(1).map(|t| t.parse::<u64>().unwrap());

    let races = time.zip(dist);

    for race in races {
        let winning_count = (0..race.0)
            .filter(|hold_time| hold_time * (race.0 - hold_time) > race.1)
            .count();

        score *= winning_count;
    }

    println!("{score}");
}


pub fn part2(input: &str) {
    let mut score = 1;

    let mut lines = input.lines();

    let time = lines.next().unwrap().split_whitespace().skip(1).collect::<Vec<&str>>().join("").parse::<u64>().unwrap();
    let dist = lines.next().unwrap().split_whitespace().skip(1).collect::<Vec<&str>>().join("").parse::<u64>().unwrap();

    let race = (time, dist);

    let winning_count = (0..race.0)
        .filter(|hold_time| hold_time * (race.0 - hold_time) > race.1)
        .count();

    score *= winning_count;

    println!("{score}");
}


#[test]
fn test() {
    part1("Time:      7  15   30
    Distance:  9  40  200");
    part1("Time:      71530
    Distance:  940200");
}