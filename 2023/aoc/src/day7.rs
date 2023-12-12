use std::collections::HashMap;
use std::hash::Hash;

#[derive(PartialOrd, Ord, PartialEq, Eq, Hash, Debug, Copy, Clone)]
enum Cards {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Farmer,
    Queen,
    King,
    Ace
}

#[derive(PartialOrd, Ord, PartialEq, Eq, Hash, Debug, Copy, Clone)]
enum CardsWithJoker {
    Joker,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Queen,
    King,
    Ace
}

#[derive(Debug, Clone)]
struct Hand<CARD> {
    pub cards: Vec<CARD>,
    pub bet: u64,
}

#[derive(PartialOrd, Ord, PartialEq, Eq, Debug, Clone)]
enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

fn get_hand_type(hand: &Hand<Cards>) -> HandType {
    let card_counts = hand.cards.iter().fold(HashMap::<Cards, u64>::new(), |mut set, card| {
        if let Some(count) = set.get(card) {
            set.insert(*card, count + 1);
        } else {
            set.insert(*card, 1);
        }
        return set;
    });
    
    if card_counts.len() == 1 {
        return HandType::FiveOfAKind;
    } else if card_counts.len() == 2 && *card_counts.values().max().unwrap() == 4 && *card_counts.values().min().unwrap() == 1 {
        return HandType::FourOfAKind;
    } else if card_counts.len() == 2 && *card_counts.values().max().unwrap() == 3 && *card_counts.values().min().unwrap() == 2 {
        return HandType::FullHouse;
    } else if card_counts.len() == 3 && card_counts.values().any(|v| *v == 3) {
        return HandType::ThreeOfAKind;
    } else if card_counts.len() == 3 && card_counts.values().filter(|v| **v == 2).count() == 2 {
        return HandType::TwoPair;
    } else if card_counts.len() == 4 {
        return HandType::OnePair;
    } else if card_counts.len() == 5 {
        return HandType::HighCard;
    } else {
        return HandType::HighCard;
    }
}

fn get_hand_type_with_joker(hand: &Hand<CardsWithJoker>) -> HandType {
    let mut card_counts = hand.cards.iter().filter(|c| **c != CardsWithJoker::Joker).fold(HashMap::<CardsWithJoker, u64>::new(), |mut set, card| {
        if let Some(count) = set.get(card) {
            set.insert(*card, count + 1);
        } else {
            set.insert(*card, 1);
        }
        return set;
    });

    let joker_count = hand.cards.iter().filter(|c| **c == CardsWithJoker::Joker).count() as u64;

    if let Some(most_common_card) = card_counts.iter().max_by_key(|(k, v)| **v) {
        if joker_count > 0 {
            card_counts.insert(*most_common_card.0, most_common_card.1 + joker_count);
        }
    } else {
        card_counts.insert(CardsWithJoker::Joker, joker_count);
    }

    
    if card_counts.len() == 1 {
        return HandType::FiveOfAKind;
    } else if card_counts.len() == 2 && *card_counts.values().max().unwrap() == 4 && *card_counts.values().min().unwrap() == 1 {
        return HandType::FourOfAKind;
    } else if card_counts.len() == 2 && *card_counts.values().max().unwrap() == 3 && *card_counts.values().min().unwrap() == 2 {
        return HandType::FullHouse;
    } else if card_counts.len() == 3 && card_counts.values().any(|v| *v == 3) {
        return HandType::ThreeOfAKind;
    } else if card_counts.len() == 3 && card_counts.values().filter(|v| **v == 2).count() == 2 {
        return HandType::TwoPair;
    } else if card_counts.len() == 4 {
        return HandType::OnePair;
    } else if card_counts.len() == 5 {
        return HandType::HighCard;
    } else {
        return HandType::HighCard;
    }
}

fn parse_card(card: char) -> Option<Cards> {
    match card {
        'A' => Some(Cards::Ace),
        'K' => Some(Cards::King),
        'Q' => Some(Cards::Queen),
        'J' => Some(Cards::Farmer),
        'T' => Some(Cards::Ten),
        '9' => Some(Cards::Nine), 
        '8' => Some(Cards::Eight),
        '7' => Some(Cards::Seven),
        '6' => Some(Cards::Six),
        '5' => Some(Cards::Five),
        '4' => Some(Cards::Four),
        '3' => Some(Cards::Three),
        '2' => Some(Cards::Two),
        _ => None,
    }
}

fn parse_card_with_joker(card: char) -> Option<CardsWithJoker> {
    match card {
        'A' => Some(CardsWithJoker::Ace),
        'K' => Some(CardsWithJoker::King),
        'Q' => Some(CardsWithJoker::Queen),
        'J' => Some(CardsWithJoker::Joker),
        'T' => Some(CardsWithJoker::Ten),
        '9' => Some(CardsWithJoker::Nine), 
        '8' => Some(CardsWithJoker::Eight),
        '7' => Some(CardsWithJoker::Seven),
        '6' => Some(CardsWithJoker::Six),
        '5' => Some(CardsWithJoker::Five),
        '4' => Some(CardsWithJoker::Four),
        '3' => Some(CardsWithJoker::Three),
        '2' => Some(CardsWithJoker::Two),
        _ => None,
    }
}

fn parse_hand(line: &str) -> Hand<Cards> {
    let mut split = line.split_whitespace();

    let cards = split.next().unwrap();
    let bet = split.next().unwrap().parse::<u64>().unwrap();

    return Hand {
        cards: cards.chars().map(|c| parse_card(c).unwrap()).collect(),
        bet: bet,
    }
}

fn parse_hand_with_joker(line: &str) -> Hand<CardsWithJoker> {
    let mut split = line.split_whitespace();

    let cards = split.next().unwrap();
    let bet = split.next().unwrap().parse::<u64>().unwrap();

    return Hand {
        cards: cards.chars().map(|c| parse_card_with_joker(c).unwrap()).collect(),
        bet: bet,
    }
}

pub fn part1(input: &str) {
    let mut hands: Vec<(HandType, Hand<Cards>)> = input.lines().map(parse_hand).map(|hand| (get_hand_type(&hand), hand)).collect();


    hands.sort_by(|a, b| {
        let ordering = a.0.cmp(&b.0);
        if ordering != std::cmp::Ordering::Equal {
            return ordering;
        }

        for i in 0..5 {
            let ordering = a.1.cards[i].cmp(&b.1.cards[i]);
            if ordering != std::cmp::Ordering::Equal {
                return ordering;
            }
        }
        return std::cmp::Ordering::Equal;
    });
        
    let score: u64 = hands.iter().map(|h| h.1.bet).zip(0..hands.len()).map(|(bet, rank)| bet * (rank as u64 + 1)).sum();
    println!("{score}");
}


pub fn part2(input: &str) {
    let mut hands: Vec<(HandType, Hand<CardsWithJoker>)> = input.lines().map(parse_hand_with_joker).map(|hand| (get_hand_type_with_joker(&hand), hand)).collect();


    hands.sort_by(|a, b| {
        let ordering = a.0.cmp(&b.0);
        if ordering != std::cmp::Ordering::Equal {
            return ordering;
        }

        for i in 0..5 {
            let ordering = a.1.cards[i].cmp(&b.1.cards[i]);
            if ordering != std::cmp::Ordering::Equal {
                return ordering;
            }
        }
        return std::cmp::Ordering::Equal;
    });
        
    let score: u64 = hands.iter().map(|h| h.1.bet).zip(0..hands.len()).map(|(bet, rank)| bet * (rank as u64 + 1)).sum();
    println!("{score}");
}


#[test]
fn test() {
    let input = "32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483";

    part1(input);
    part2(input);
}