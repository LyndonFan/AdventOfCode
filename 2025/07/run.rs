// use std::env;
use std::fs;
use std::collections::{HashSet, HashMap};

fn main() {
    // println!("testing internal functions");
    // let passed_tests = test_part_b();
    // if !passed_tests {
    //     return;
    // }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(input) = {}", test_input.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 21", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 40", test_res);

    println!("Reading input.txt");
    let live_contents = fs::read_to_string("input.txt").expect("Should have been able to read input file");
    let live_input = parse(&live_contents);
    println!("len(input) = {}", live_input.len());
    let mut live_res = part_a(live_input.clone());
    println!("Part a live res: {}", live_res);
    live_res = part_b(live_input.clone());
    println!("Part b live res: {}", live_res);
}

fn parse(contents: &String) -> Vec<&str> {
    contents.trim().split("\n").collect()
}

fn part_a(parts: Vec<&str>) -> i64 {
    let mut res = 0;
    let mut indexes = HashSet::new();
    let n = parts[0].len();
    let should_print_debug_messages = n <= 20;
    for (i, c) in parts[0].chars().into_iter().enumerate() {
        if c == 'S' {
            indexes.insert(i);
            if should_print_debug_messages {
                println!("found start at {}", i);
            }
            break;
        }
    }
    for (r, line) in parts[1..parts.len()].into_iter().enumerate() {
        let mut new_indexes = HashSet::new();
        let bytes: Vec<_> = line.bytes().collect();
        for i in indexes.into_iter() {
            if bytes[i] != b'^' {
                new_indexes.insert(i);
                continue;
            }
            res += 1;
            if should_print_debug_messages {
                println!("found split at ({}, {})", r+1, i);
            }
            if i > 0 {
                new_indexes.insert(i-1);
            }
            if i < n-1 {
                new_indexes.insert(i+1);
            }
        }
        indexes = new_indexes;
    }
    res
}

fn part_b(parts: Vec<&str>) -> i64 {
    let mut timelines = HashMap::<usize, i64>::new();
    let n = parts[0].len();
    let should_print_debug_messages = n <= 20;
    for (i, c) in parts[0].chars().into_iter().enumerate() {
        if c == 'S' {
            timelines.insert(i, 1);
            if should_print_debug_messages {
                println!("found start at {}", i);
            }
            break;
        }
    }
    for (r, line) in parts[1..parts.len()].into_iter().enumerate() {
        let mut new_timelines = HashMap::<usize, i64>::new();
        let bytes: Vec<_> = line.bytes().collect();
        for (i, t) in timelines {
            if bytes[i] != b'^' {
                new_timelines.entry(i).and_modify(|v| *v = *v+t).or_insert(t);
                continue;
            }
            if should_print_debug_messages {
                println!("found split at ({}, {})", r+1, i);
            }
            if i > 0 {
                new_timelines.entry(i-1).and_modify(|v| *v = *v+t).or_insert(t);
            }
            if i < n-1 {
                new_timelines.entry(i+1).and_modify(|v| *v = *v+t).or_insert(t);
            }
        }
        if should_print_debug_messages {
            println!("{:?}", new_timelines);
        }
        timelines = new_timelines;
    }
    let mut res = 0;
    for v in timelines.values() {
        res += v;
    }
    res
}
