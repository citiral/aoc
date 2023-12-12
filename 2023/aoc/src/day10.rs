use std::collections::HashSet;

#[derive(PartialEq, Eq, Copy, Clone)]
enum Direction {
    North,
    East,
    South,
    West
}

type Pipe = [Direction;2];

enum Tile {
    Pipe(Pipe),
    Start
}

impl Direction {
    fn flip(&self) -> Direction {
        match self {
            Direction::North => Direction::South,
            Direction::South => Direction::North,
            Direction::East => Direction::West,
            Direction::West => Direction::East,
        }
    }

    fn next(&self) -> Direction {
        match self {
            Direction::North => Direction::East,
            Direction::East => Direction::South,
            Direction::South => Direction::West,
            Direction::West => Direction::North,
        }
    }

    fn dx(&self) -> i32 {
        match self {
            Direction::North => 0,
            Direction::East => 1,
            Direction::South => 0,
            Direction::West => -1,
        }
    }

    fn dy(&self) -> i32 {
        match self {
            Direction::North => -1,
            Direction::East => 0,
            Direction::South => 1,
            Direction::West => 0,
        }
    }
}

fn parse_char(c: char) -> Option<Tile> {
    match c {
        '|' => Some(Tile::Pipe([Direction::North, Direction::South])),
        '-' => Some(Tile::Pipe([Direction::East, Direction::West])),
        'L' => Some(Tile::Pipe([Direction::North, Direction::East])),
        'J' => Some(Tile::Pipe([Direction::North, Direction::West])),
        '7' => Some(Tile::Pipe([Direction::South, Direction::West])),
        'F' => Some(Tile::Pipe([Direction::South, Direction::East])),
        'S' => Some(Tile::Start),
        _ => None,
    }
}

fn get_start_coordinates(map: &Vec<Vec<Option<Tile>>>) -> Option<(usize, usize)> {
    for y in 0..map.len() {
        for x in 0..map[y].len() {
            if let Some(ref tile) = map[y][x] {
                match tile {
                    Tile::Start => return Some((x, y)),
                    _ => {},
                }
            }
        }
    }

    return None;
}


fn get_loop_length(map: &Vec<Vec<Option<Tile>>>, start: (usize, usize)) -> usize {
    let mut length = 0;

    let mut current = start;
    let mut next_dir = Direction::North;

    for _ in 0..4 {
        if let Some(Tile::Pipe(pipe)) = &map[(current.1 as i32 + next_dir.dy()) as usize][(current.0 as i32 + next_dir.dx()) as usize] {
            if pipe.iter().any(|d| d.flip() == next_dir) {
                break;
            }
        } else {
            next_dir = next_dir.next();
        }
    }

    loop {
        match &map[(current.1 as i32 + next_dir.dy()) as usize][(current.0 as i32 + next_dir.dx()) as usize] {
            Some(Tile::Pipe(pipe)) => {
                current.0 = (current.0 as i32 + next_dir.dx()) as usize;
                current.1 = (current.1 as i32 + next_dir.dy()) as usize;
                next_dir = *pipe.iter().filter(|d| d.flip() != next_dir).next().unwrap();
                length += 1;
            },
            Some(Tile::Start) => {
                return length;
            },
            _ => {
                println!("Error, unexpected tile type in loop,");
                return 0;
            }
        }
    }
}


fn get_pipes_in_loop(map: &Vec<Vec<Option<Tile>>>, start: (usize, usize)) -> Vec<(usize, usize)> {
    let mut pipes: Vec<(usize, usize)> = Vec::new();

    let mut current = start;
    let mut next_dir = Direction::North;

    for _ in 0..4 {
        if let Some(Tile::Pipe(pipe)) = &map[(current.1 as i32 + next_dir.dy()) as usize][(current.0 as i32 + next_dir.dx()) as usize] {
            if pipe.contains(&next_dir.flip()) {
                break;
            }
        }
        next_dir = next_dir.next();
    }

    loop {
        match &map[(current.1 as i32 + next_dir.dy()) as usize][(current.0 as i32 + next_dir.dx()) as usize] {
            Some(Tile::Pipe(pipe)) => {
                pipes.push(current);

                current.0 = (current.0 as i32 + next_dir.dx()) as usize;
                current.1 = (current.1 as i32 + next_dir.dy()) as usize;
                
                next_dir = *pipe.iter().filter(|d| d.flip() != next_dir).next().unwrap();
            },
            Some(Tile::Start) => {
                pipes.push(current);
                return pipes;
            },
            _ => {
                return pipes;
            }
        }
    }
}


pub fn part1(input: &str) {
    let map: Vec<Vec<Option<Tile>>> = input.lines().map(|l| l.chars().map(parse_char).collect()).collect();
    
    if let Some(start)= get_start_coordinates(&map) {
        let length = get_loop_length(&map, start);
        if length % 2 == 0 {
            println!("{}", length / 2);
        } else {
            println!("{}", (length+1) / 2);
        }
    } else {
        println!("No start coordinate found?");
    }
}


fn get_inside_parts(map: &Vec<Vec<Option<Tile>>>, pipemap: &Vec<Vec<bool>>) -> HashSet<(usize, usize)> {
    let mut output = HashSet::<(usize, usize)>::new();

    for y in 0..map.len() {
        let mut inside = false;
        let mut in_horiz = false;
        let mut horiz_enter: Direction = Direction::North;

        for x in 0..map[y].len() {

            match pipemap[y][x] {
                true => {
                    if let Some(Tile::Pipe(ref dirs)) = map[y][x] {
                        if !in_horiz && dirs.contains(&Direction::East) {
                            in_horiz = true;
                            horiz_enter = *dirs.iter().filter(|&d| *d != Direction::East).next().unwrap();
                            match horiz_enter {
                                Direction::East => print!("e"),
                                Direction::North => print!("n"),
                                Direction::South => print!("s"),
                                Direction::West => print!("w"),
                            }
                        }
                        else if in_horiz && !dirs.contains(&Direction::East) {
                            in_horiz = false;
                            let output_dir = *dirs.iter().filter(|&d| *d != Direction::West).next().unwrap();

                            if horiz_enter != output_dir {
                                inside = !inside;
                                if inside {
                                    print!("E");
                                } else {
                                    print!("X");
                                }
                            } else {
                                if inside {
                                    print!("E");
                                } else {
                                    print!("X");
                                }
                            }
                        } else if !in_horiz {
                            inside = !inside;
                            if inside {
                                print!("E");
                            } else {
                                print!("X");
                            }
                        } else {
                            print!("-");
                        }
                    } else {
                        inside = !inside;
                    }
                },
                false => {
                    if inside {
                        output.insert((x, y));
                        print!("I");
                    } else {
                        print!(".");
                    }
                }
            }
        }
        println!("");
    }

    output
}


pub fn part2(input: &str) {
    let mut map: Vec<Vec<Option<Tile>>> = input.lines().map(|l| l.chars().map(parse_char).collect()).collect();
    
    if let Some(start)= get_start_coordinates(&map) {
        let pipes = get_pipes_in_loop(&map, start);
        let mut pipemap:Vec<Vec<bool>> = Vec::new();

        for y in 0..map.len() {
            pipemap.push(Vec::<bool>::new());
            for _ in 0..map[y].len() {
                pipemap[y].push(false);
            }
        }

        let mut newstart = Vec::new();

        for pipe in pipes {
            pipemap[pipe.1][pipe.0] = true;
        }
        if let Some(Tile::Pipe(dir)) = map[start.1+1][start.0] {
            if dir.contains(&Direction::North) {
                newstart.push(Direction::South);
            }
        }
        if let Some(Tile::Pipe(dir)) = map[start.1-1][start.0] {
            if dir.contains(&Direction::South) {
                newstart.push(Direction::North);
            }
        }
        if let Some(Tile::Pipe(dir)) = map[start.1][start.0+1] {
            if dir.contains(&Direction::West) {
                newstart.push(Direction::East);
            }
        }
        if let Some(Tile::Pipe(dir)) = map[start.1][start.0-1] {
            if dir.contains(&Direction::East) {
                newstart.push(Direction::West);
            }
        }

        map[start.1][start.0] = Some(Tile::Pipe([newstart[0], newstart[1]]));

        let inside = get_inside_parts(&map, &pipemap);
        
        for y in 0..map.len() {
            for x in 0..map[y].len() {
                if pipemap[y][x] {
                    print!("#");
                } else {
                    print!(".");
                }
            }
            println!("");
        }

        println!("{}", inside.len());

    } else {
        println!("No start coordinate found?");
    }
}


#[test]
fn test() {
    
    part1("7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ");

    part2("....................
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L");
}