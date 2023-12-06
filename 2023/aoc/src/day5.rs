#[derive(Debug)]
struct Mapping{
    pub from: u64,
    pub to: u64,
    pub range: u64
}

#[derive(Debug)]
struct Range {
    pub start: u64,
    pub range: u64,
}

pub fn part1(input: &str) {
    let mut lines = input.lines();

    let seeds = lines.next().unwrap().split_whitespace().skip(1).map(|seed| seed.parse::<u64>().unwrap());
    let mut ranges: Vec<Range> = seeds.map(|seed| {
        Range {
            start: seed,
            range: 1
        }
    }).collect();

    lines.next();

    println!("{:?}", ranges);

    while let Some(header) = lines.next() {
        println!("{}", header);
        let mut mappings = Vec::<Mapping>::new();

        while let Some(line) = lines.next() {
            if line.trim().is_empty() {
                break;
            }

            let values: Vec<u64> = line.split_whitespace().map(|entry| entry.parse::<u64>().unwrap()).collect();
            mappings.push(Mapping {
                from: values[1],
                to: values[0],
                range: values[2],
            });
        }
        
        let mut new_ranges: Vec<Range> = Vec::new();
        for range in ranges.iter() {
            let mut index = range.start;
            let mut remaining = range.range;

            while remaining > 0 {

                let mut actual_mapping = mappings.iter().filter(|mapping| mapping.from <= index && mapping.from + mapping.range > index);
                if let Some(mapping) = actual_mapping.next() {
                    let range = u64::min(remaining, mapping.from + mapping.range - index);
                    new_ranges.push(Range {
                        start: mapping.to + (index - mapping.from),
                        range: range,
                    });
                    index += range;
                    remaining -= range;
                } else {
                    let soonest_maping = mappings.iter().filter(|mapping| mapping.from > index).min_by_key(|mapping| mapping.from);
                    if let Some(mapping) = soonest_maping {
                        let range = u64::min(remaining, mapping.from - index);
                        new_ranges.push(Range {
                            start: index,
                            range: range,
                        });
                        index += range;
                        remaining -= range;
                    } else {
                        new_ranges.push(Range {
                            start: index,
                            range: remaining,
                        });

                        index += remaining;
                        remaining = 0;
                    }
                }
            }            
        }

        ranges = new_ranges;
    }

    println!("{:?}", ranges.iter().map(|r| r.start).min());
}


pub fn part2(input: &str) {
    let mut lines = input.lines();

    let seeds: Vec<u64> = lines.next().unwrap().split_whitespace().skip(1).map(|seed| seed.parse::<u64>().unwrap()).collect();
    let mut ranges: Vec<Range> = Vec::new();
    for i in (0..seeds.len()).step_by(2) {
        ranges.push(Range {
            start: seeds[i],
            range: seeds[i+1]
        });
    }

    lines.next();

    println!("{:?}", ranges);

    while let Some(header) = lines.next() {
        println!("{}", header);
        let mut mappings = Vec::<Mapping>::new();

        while let Some(line) = lines.next() {
            if line.trim().is_empty() {
                break;
            }

            let values: Vec<u64> = line.split_whitespace().map(|entry| entry.parse::<u64>().unwrap()).collect();
            mappings.push(Mapping {
                from: values[1],
                to: values[0],
                range: values[2],
            });
        }
        
        let mut new_ranges: Vec<Range> = Vec::new();
        for range in ranges.iter() {
            let mut index = range.start;
            let mut remaining = range.range;

            while remaining > 0 {

                let mut actual_mapping = mappings.iter().filter(|mapping| mapping.from <= index && mapping.from + mapping.range > index);
                if let Some(mapping) = actual_mapping.next() {
                    let range = u64::min(remaining, mapping.from + mapping.range - index);
                    new_ranges.push(Range {
                        start: mapping.to + (index - mapping.from),
                        range: range,
                    });
                    index += range;
                    remaining -= range;
                } else {
                    let soonest_maping = mappings.iter().filter(|mapping| mapping.from > index).min_by_key(|mapping| mapping.from);
                    if let Some(mapping) = soonest_maping {
                        let range = u64::min(remaining, mapping.from - index);
                        new_ranges.push(Range {
                            start: index,
                            range: range,
                        });
                        index += range;
                        remaining -= range;
                    } else {
                        new_ranges.push(Range {
                            start: index,
                            range: remaining,
                        });

                        index += remaining;
                        remaining = 0;
                    }
                }
            }            
        }

        ranges = new_ranges;
    }

    println!("{:?}", ranges.iter().map(|r| r.start).min());
}


#[test]
fn test() {
    let input ="seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4";

    part1(input);
    part2(input);
}