use std::collections::HashMap;

enum Instruction {
    Left,
    Right
}

pub fn part1(input: &str) {
    let mut lines = input.lines();

    let instructions = lines.next().unwrap().chars().map(|c| match c {
        'L' => Some(Instruction::Left),
        'R' => Some(Instruction::Right),
        _ => None,
    }.unwrap()).collect::<Vec<Instruction>>();

    let locations = lines.skip(1).map(|line| {
        let mut s1 = line.split("=");
        let from = s1.next().unwrap().trim();

        let mut next = s1.next().unwrap().trim();
        let mut to = next[1..next.len() - 1].split(",").map(|l| l.trim());

        return (from, (to.next().unwrap(), to.next().unwrap()));
    }).collect::<HashMap<&str, (&str, &str)>>();

    let mut current = "AAA";
    let mut instr_index = 0;
    let mut step_count = 0;

    while current != "ZZZ" {
        let instruction = &instructions[instr_index];

        match instruction {
            Instruction::Left => current = locations[current].0,
            Instruction::Right => current = locations[current].1,
        };

        instr_index += 1;
        if instr_index >= instructions.len() {
            instr_index = 0;
        }

        step_count += 1;
    }
        
    println!("{step_count}");
}


fn calculate_path_offset_repeat_and_loop(instructions: &Vec<Instruction>, locations: &HashMap<&str, (&str, &str)>, start: &str) -> (usize, usize) {
    let mut current = start;
    let mut instr_index: usize = 0;
    let mut step_count: usize = 0;

    while !current.ends_with('Z') {
        let instruction = &instructions[instr_index];

        match instruction {
            Instruction::Left => current = locations[current].0,
            Instruction::Right => current = locations[current].1,
        };

        instr_index += 1;
        if instr_index >= instructions.len() {
            instr_index = 0;
        }

        step_count += 1;
    }

    let mut force_step = true;
    let mut step_count_2: usize = 0;
    while !current.ends_with('Z') || force_step {
        force_step = false;
        let instruction = &instructions[instr_index];

        match instruction {
            Instruction::Left => current = locations[current].0,
            Instruction::Right => current = locations[current].1,
        };

        instr_index += 1;
        if instr_index >= instructions.len() {
            instr_index = 0;
        }

        step_count_2 += 1;
    }

    return (step_count - step_count_2, step_count_2);
}


pub fn part2(input: &str) {
    let mut lines = input.lines();

    let instructions = lines.next().unwrap().chars().map(|c| match c {
        'L' => Some(Instruction::Left),
        'R' => Some(Instruction::Right),
        _ => None,
    }.unwrap()).collect::<Vec<Instruction>>();

    let locations = lines.skip(1).map(|line| {
        let mut s1 = line.split("=");
        let from = s1.next().unwrap().trim();

        let mut next = s1.next().unwrap().trim();
        let mut to = next[1..next.len() - 1].split(",").map(|l| l.trim());

        return (from, (to.next().unwrap(), to.next().unwrap()));
    }).collect::<HashMap<&str, (&str, &str)>>();

    let mut current: Vec<&str> = locations.keys().filter(|k| k.ends_with('A')).map(|v| *v).collect();
    let mut steps: Vec<usize> = current.iter().map(|c| calculate_path_offset_repeat_and_loop(&instructions, &locations, *c)).map(|v| v.1).collect();
    let min_step = steps.iter().min().unwrap();

    /*let mut step = steps[0];

    while steps.iter().any(|s| step % s != 0) {
        step += min_step;
    }*/

    println!("Use Wolfram Alpha to find LCM of: {steps:?} :)");
}


#[test]
fn test() {
    let input = "RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)";
    
    part1(input);
    let input = "LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)";    
    part1(input);

    let input = "LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)";
    part2(input);
}