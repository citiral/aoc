use std::collections::HashMap;

#[derive(Copy, Clone, Debug, PartialEq, Eq)]
enum Spring {
    Damaged,
    Operational,
    Unknown
}

fn get_arrangements_rec(springs: &Vec<Spring>, index: usize) -> Vec<Vec<Spring>> {
    if index >= springs.len() {
        return vec![Vec::new()];
    }
    
    match springs[index] {
        Spring::Damaged => {
            let mut arrangements = get_arrangements_rec(springs, index + 1);
            for a in arrangements.iter_mut() {
                a.push(Spring::Damaged);
            }
            arrangements
        },
        
        Spring::Operational => {
            let mut arrangements = get_arrangements_rec(springs, index + 1);
            for a in arrangements.iter_mut() {
                a.push(Spring::Operational);
            }
            arrangements
        },

        Spring::Unknown => {
            let mut arrangements = get_arrangements_rec(springs, index + 1);
            let mut result: Vec<Vec<Spring>> = Vec::new();

            for a in arrangements.iter_mut() {
                let mut c = a.clone();
                c.push(Spring::Operational);
                a.push(Spring::Damaged);
                result.push(c);
                result.push(a.clone());
            }
            
            result
        }
    }
}

fn does_arrangement_match(arrangement: &Vec<Spring>, record: &Vec<usize>) -> bool
{
    let split = arrangement.split(|s| *s == Spring::Operational).filter(|l| l.len() > 0).collect::<Vec<_>>();
    if split.len() == record.len() {
        split.iter().map(|l| l.len()).zip(record).all(|(a, b)| a == *b)
    } else {
        false
    }
}

pub fn part1(input: &str) {
    let mut score = 0;

    for line in input.lines() {
        let mut parts = line.split_whitespace();
        
        let springs = parts.next().unwrap().chars().map(|c| match c {
            '.' => Spring::Operational,
            '#' => Spring::Damaged,
            _ => Spring::Unknown
        }).collect::<Vec<_>>();
        let record= parts.next().unwrap().split(",").map(|n| n.parse::<usize>().unwrap()).collect::<Vec<_>>();

        let arrangements = get_arrangement_counts(&springs, &record);

        score += arrangements;
        println!("{line} -> {arrangements}");
    }

    println!("{score}");
}


pub fn part2(input: &str) {
    let mut score = 0;

    for line in input.lines() {
        let mut parts = line.split_whitespace();
        
        let springs = vec![parts.next().unwrap()].repeat(5).join("?").chars().map(|c| match c {
            '.' => Spring::Operational,
            '#' => Spring::Damaged,
            _ => Spring::Unknown
        }).collect::<Vec<_>>();

        let record= vec![parts.next().unwrap()].repeat(5).join(",").split(",").map(|n| n.parse::<usize>().unwrap()).collect::<Vec<_>>();

        let arrangements = get_arrangement_counts(&springs, &record);

        score += arrangements;
        println!("{line} -> {arrangements}");
    }

    println!("{score}");
}


#[test]
fn test() {
    let input = "???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1";

    part1(input);
    part2(input);
}

fn get_arrangement_counts_rec(springs: &Vec<Spring>, record: &Vec<usize>, spring_index: usize, record_index: usize, running_length: usize, cache: &mut HashMap<(usize, usize, usize), usize>) -> usize {
    if let Some(cached) = cache.get(&(spring_index, record_index, running_length)) {
        return *cached;
    }
    
    if spring_index >= springs.len() {
        if record_index == record.len() - 1 && *record.last().unwrap() == running_length {
            return 1;
        } else if record_index >= record.len() {
            return 1;
        } else {
            return 0;
        }
    }

    let result = match springs[spring_index] {
        Spring::Damaged => {
            if record_index >= record.len() || running_length + 1 > record[record_index] {
                0
            } else {
                get_arrangement_counts_rec(springs, record, spring_index + 1, record_index, running_length + 1, cache)
            }
        },
        
        Spring::Operational => {
            if running_length > 0 {
                if running_length != record[record_index] {
                    0
                } else {
                    get_arrangement_counts_rec(springs, record, spring_index + 1, record_index + 1, 0, cache)
                }
            } else {
                get_arrangement_counts_rec(springs, record, spring_index + 1, record_index, 0, cache)
            }
        },

        Spring::Unknown => {
            let damaged_count = if record_index >= record.len() || running_length + 1 > record[record_index] {
                0
            } else {
                get_arrangement_counts_rec(springs, record, spring_index + 1, record_index, running_length + 1, cache)
            };

            let operation_count = if running_length > 0 {
                if running_length != record[record_index] {
                    0
                } else {
                    get_arrangement_counts_rec(springs, record, spring_index + 1, record_index + 1, 0, cache)
                }
            } else {
                get_arrangement_counts_rec(springs, record, spring_index + 1, record_index, 0, cache)
            };

            damaged_count + operation_count
        }
    };

    cache.insert((spring_index, record_index, running_length), result);

    return result;

}

fn get_arrangement_counts(springs: &Vec<Spring>, record: &Vec<usize>) -> usize {
    let mut cache = HashMap::new();
    return get_arrangement_counts_rec(springs, record, 0, 0, 0, &mut cache);
}