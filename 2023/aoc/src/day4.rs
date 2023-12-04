use std::collections::{HashSet, HashMap};

pub fn part1(input: &str) {
    let mut score = 0;

    for line in input.lines() {
        let mut split = line.split('|');

        let winning_numbers: HashSet<i32> = split
            .next()
            .unwrap()
            .split(":")
            .skip(1)
            .next()
            .unwrap()
            .trim()
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap())
            .collect();

        let present_numbers = split
            .next()
            .unwrap()
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap());

        let mut line_score = 0;
        for number in present_numbers {
            if winning_numbers.contains(&number) {
                line_score = match line_score {
                    0 => 1,
                    _ => line_score * 2,
                }
            }
        }

        score += line_score;
    }

    println!("{score}");
}


pub fn part2(input: &str) {
    let mut copies: HashMap<usize, i32> = HashMap::new();

    for (i, line) in input.lines().enumerate() {         
        let this_card_count = if let Some(count) = copies.get(&i) {
            count + 1
        } else {
            1
        };
        copies.insert(i, this_card_count);
            
        let mut split = line.split('|');

        let winning_numbers: HashSet<i32> = split
            .next()
            .unwrap()
            .split(":")
            .skip(1)
            .next()
            .unwrap()
            .trim()
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap())
            .collect();

        let present_numbers = split
            .next()
            .unwrap()
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap());

        let mut offset = 1;
        for number in present_numbers {
            if winning_numbers.contains(&number) {
                let won_card_count = copies.get(&(i + offset)).copied().unwrap_or(0);
                copies.insert(i + offset, won_card_count + this_card_count);
                offset += 1;
            }
        }
    }

    let score: i32 = copies.values().sum();
    println!("{score}");
}


#[test]
fn test() {
    part1("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11");

part2("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11");
}