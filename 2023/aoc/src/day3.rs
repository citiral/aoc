
fn has_symbol(line: Option<&str>, start: usize, end: usize) -> bool {
    line.map_or(false, |line| {
        line.chars().skip(start).take(end - start + 1).any(|c| c != '.' && !c.is_numeric())
    })
}

fn check_number(lines: &Vec<&str>, line_index: usize, mut start: usize, mut end: usize) -> bool {
    if start > 0 {
        start -= 1;
    }
    end += 1;

    if line_index > 0 && has_symbol(lines.get(line_index-1).copied(), start, end) {
        true
    } else if has_symbol(lines.get(line_index).copied(), start, end) {
        true
    } else if has_symbol(lines.get(line_index+1).copied(), start, end) {
        true
    } else {
        false
    }
}

pub fn part1(input: &str) {
    let mut sum = 0;
    let mut lines: Vec<&str> = input.lines().collect();

    for (line_index, line) in lines.iter().enumerate() {

        let mut span_start: Option<usize> = None;
        let mut span_end: Option<usize> = None;
        let mut value = 0;

        for (i, char) in line.char_indices() {
            if char.is_numeric() {
                if span_start.is_none() {
                    span_start = Some(i);
                }
                span_end = Some(i);
                value = value * 10 + char.to_digit(10).unwrap();
            } else {
                if value > 0 {
                    if let Some(start) = span_start {
                        if let Some(end) = span_end {
                            if check_number(&lines, line_index, start, end) {
                                sum += value;
                            }
                        }
                    }   
                }
                
                value = 0;
                span_start = None;
                span_end = None;
            }
        }

        if value > 0 {
            if let Some(start) = span_start {
                if let Some(end) = span_end {
                    if check_number(&lines, line_index, start, end) {
                        sum += value;
                    }   
                }
            }   
        }
    }

    println!("{sum}");
}


fn get_gear_score(lines: &Vec<&str>, gear_x: usize, gear_y: usize) -> u32 {
    let mut count = 0;
    let mut score = 1;

    for i in gear_y as i32 - 1 .. gear_y as i32 + 2 {
        if i >= 0 {
            let line = lines[i as usize];

            let mut span_start: Option<usize> = None;
            let mut span_end: Option<usize> = None;
            let mut value = 0;
    
            for (i, char) in line.char_indices() {
                if char.is_numeric() {
                    if span_start.is_none() {
                        span_start = Some(i);
                    }
                    span_end = Some(i);
                    value = value * 10 + char.to_digit(10).unwrap();
                } else {
                    if value > 0 {
                        if let Some(start) = span_start {
                            if let Some(end) = span_end {
                                if gear_x + 1 >= start && gear_x <= end + 1 {
                                    score *= value;
                                    count += 1;
                                }
                            }
                        }
                    }
                    
                    value = 0;
                    span_start = None;
                    span_end = None;
                }
            }
    
            if value > 0 {
                if let Some(start) = span_start {
                    if let Some(end) = span_end {
                        if gear_x + 1 >= start && gear_x <= end + 1 {
                            score *= value;
                            count += 1;
                        }
                    }
                }
            }
        }
    }

    if count > 1 {
        score
    } else {
        0
    }
}


pub fn part2(input: &str) {
    let mut sum = 0;
    let lines: Vec<&str> = input.lines().collect();

    for (line_index, line) in lines.iter().enumerate() {
        for (char_index, char) in line.char_indices() {
            if char == '*' {
                sum += get_gear_score(&lines, char_index, line_index);
            }
        }
    }

    println!("{sum}");
}


#[test]
fn test() {
    part1("467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..");

part2("467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..");
}