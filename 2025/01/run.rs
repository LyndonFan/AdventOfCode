// use std::env;
use std::fs;

fn main() {
    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(test_input) = {}", test_input.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 3", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 6", test_res);

    println!("Reading input.txt");
    let live_contents = fs::read_to_string("input.txt").expect("Should have been able to read input file");
    let live_input = parse(&live_contents);
    println!("len(live_input) = {}", live_input.len());
    let mut live_res = part_a(live_input.clone());
    println!("Part a live res: {}", live_res);
    live_res = part_b(live_input.clone());
    println!("Part b live res: {}", live_res);
}

fn parse(contents: &String) -> Vec<&str> {
    let mut res: Vec<&str> = contents.split('\n').collect();
    res.pop();
    res
}

fn part_a(lines: Vec<&str>) -> i32 {
    let mut dial = 50;
    let mut res = 0;
    for &line in lines.iter() {
        let mut sign = 1;
        if line.chars().nth(0).unwrap() == 'L' {
            sign = -1;
        }
        let steps = line[1..].parse::<i32>().unwrap();
        dial = (dial + sign * steps) % 100;
        if dial == 0 {
            res += 1;
        }
    }
    res
}

fn part_b(lines: Vec<&str>) -> i32 {
    let mut dial = 50;
    let mut res = 0;
    for &line in lines.iter() {
        let mut sign = 1;
        if line.chars().nth(0).unwrap() == 'L' {
            sign = -1;
        }
        let mut steps = line[1..].parse::<i32>().unwrap();
        res += steps / 100;
        steps %= 100;
        let dial_start = dial;
        if steps > 0 {
            dial += sign * steps;
            if dial < 0 {
                dial += 100;
                if dial_start > 0 {
                    res += 1;
                }
            } else if dial == 0 {
                res += 1;
            } else if dial >= 100 {
                dial -= 100;
                res += 1;
            }
        }
        if lines.len() <= 10 {
            println!("line = {}, dial = {}, res = {}", line, dial, res);
        }
    }
    res
}

// >4576, <6795