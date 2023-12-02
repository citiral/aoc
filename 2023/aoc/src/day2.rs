pub fn part1(input: &str) {
    let mut score = 0;

    for game in input.lines() {
        let start_index = game.find(':').unwrap();
        let id = &game[5..start_index].parse::<i32>().unwrap();

        let possible = game[start_index+1..]
            .split(';')
            .map(|h| h.trim())
            .map(|h| {
                h.split(", ")
                 .map(|color| {
                    let mut split = color.split(' ');
                    (split.next().unwrap().parse::<u32>().unwrap(), split.next().unwrap())
                })
                 .map(|(count, color)| match color {
                    "red" => count <= 12,
                    "green" => count <= 13,
                    "blue" => count <= 14,
                    _ => panic!("Invalid color {}", color)
                 })
                 .all(|x| x)
            })
            .all(|x| x);

        if possible {
            score += id
        }
    }
    
    println!("{score}");
}

pub fn part2(input: &str) {
    let mut score = 0;

    for game in input.lines() {
        let start_index = game.find(':').unwrap();
        let id = &game[5..start_index].parse::<i32>().unwrap();

        let mut options: Vec<(u32, &str)> = game[start_index+1..]
            .split(';')
            .map(|h| h.trim())
            .flat_map(|h| h.split(", "))
            .map(|color| {
                let mut split = color.split(' ');
                (split.next().unwrap().parse::<u32>().unwrap(), split.next().unwrap())
            }).collect();

        let max_red = options.iter().filter(|(_, color)| *color == "red").map(|(count, _)| *count).max().unwrap();
        let max_green = options.iter().filter(|(_, color)| *color == "green").map(|(count, _)| *count).max().unwrap();
        let max_blue = options.iter().filter(|(_, color)| *color == "blue").map(|(count, _)| *count).max().unwrap();
        
        score += max_red * max_green * max_blue;
    }
    
    println!("{score}");
}


#[test]
fn test() {
    part2("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
}