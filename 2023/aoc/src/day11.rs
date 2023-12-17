fn get_row_map(input: &str, expansion_factor: usize) -> Vec<usize> {
    let mut row_map = Vec::<usize>::new();
    let mut cur_row = 0;

    for line in input.lines() {
        row_map.push(cur_row);

        if line.chars().all(|c| c == '.') {
            cur_row += expansion_factor;
        } else {
            cur_row += 1;
        }
    }

    row_map
}


fn get_col_map(input: &str, expansion_factor: usize) -> Vec<usize> {
    let mut col_map = Vec::<usize>::new();
    let mut cur_col = 0;
    let lines: Vec<&str> = input.lines().collect();
    let line_length = lines[0].len();

    for x in 0..line_length {
        col_map.push(cur_col);
        if (0..lines.len()).all(|line| lines[line].chars().skip(x).next().unwrap() == '.') {
            cur_col += expansion_factor;
        } else {
            cur_col += 1;
        }
    }
    
    col_map
}


fn run(input: &str, expansion_factor: usize) {
    let col_map = get_col_map(input, expansion_factor);
    let row_map = get_row_map(input, expansion_factor);

    let lines: Vec<&str> = input.lines().collect();

    let mut galaxies: Vec<(usize, usize)> = Vec::new();
    for y in 0..lines.len() {
        for x in 0..lines[y].len() {
            if lines[y].chars().skip(x).next().unwrap() == '#' {
                galaxies.push((col_map[x], row_map[y]));
            }
        }
    }

    let mut score = 0;
    for a in 0..galaxies.len() {
        for b in a+1..galaxies.len() {
            score += galaxies[a].0.abs_diff(galaxies[b].0) + galaxies[a].1.abs_diff(galaxies[b].1);
        }
    }

    println!("{score}");
}


pub fn part1(input: &str) {
    run(input, 2);
}


pub fn part2(input: &str) {
    run(input, 1000000);
}


#[test]
fn test() {
    let input = "...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....";
    part1(input);

    part2(input);
}
