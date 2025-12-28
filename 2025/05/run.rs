// use std::env;
use std::fs;

fn main() {
    println!("testing internal functions");
    let passed_tests = test_part_b();
    if !passed_tests {
        return;
    }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(input.ranges) = {}", test_input.ranges.len());
    println!("len(input.items) = {}", test_input.items.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 3", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 14", test_res);

    println!("Reading input.txt");
    let live_contents = fs::read_to_string("input.txt").expect("Should have been able to read input file");
    let live_input = parse(&live_contents);
    println!("len(input.ranges) = {}", live_input.ranges.len());
    println!("len(input.items) = {}", live_input.items.len());
    let mut live_res = part_a(live_input.clone());
    println!("Part a live res: {}", live_res);
    live_res = part_b(live_input.clone());
    println!("Part b live res: {}", live_res);
}

#[derive(Debug, Clone)]
struct RangesAndItems {
    ranges: Vec<Vec<i64>>,
    items: Vec<i64>,
}

impl RangesAndItems {
    fn sort(&mut self) {
        self.ranges.sort();
        self.items.sort();
    }
}

fn parse(contents: &String) -> RangesAndItems {
    let parts: Vec<&str> = contents.trim().split("\n\n").collect();
    let items: Vec<i64> = parts[1].split('\n').collect::<Vec<_>>().iter().map(|x| x.parse::<i64>().unwrap()).collect();
    let ranges_strings: Vec<_> = parts[0].split('\n').collect();
    let mut ranges: Vec<Vec<i64>> = vec![vec![0; 2]; ranges_strings.len()];
    for (i, s) in ranges_strings.iter().enumerate() {
        ranges[i] = s.split('-').collect::<Vec<_>>().iter().map(|x| x.parse::<i64>().unwrap()).collect();
    }
    RangesAndItems{
        ranges: ranges,
        items: items,
    }
}

fn part_a(ranges_and_items: RangesAndItems) -> i64 {
    let mut ranges_and_items = ranges_and_items;
    ranges_and_items.sort();
    let should_print_debug_messages = ranges_and_items.ranges.len() <= 10;
    if should_print_debug_messages {
        println!("ranges: {:?}", ranges_and_items.ranges);
        println!("items: {:?}", ranges_and_items.items);
    }
    let ranges = ranges_and_items.ranges;
    let items = ranges_and_items.items;
    let mut res = 0;
    let mut idx = 0;
    let m = ranges.len();
    for item in items {
        if idx == m {
            break;
        }
        if item < ranges[idx][0] {
            continue;
        }
        let mut found_range = false;
        while idx < m && item >= ranges[idx][0] && !found_range {
            found_range = item <= ranges[idx][1];
            if !found_range {
                idx += 1;
            }
        }
        if found_range {
            res += 1;
        }
    }
    res
}

fn part_b(ranges_and_items: RangesAndItems) -> i64 {
    let mut ranges_and_items = ranges_and_items;
    ranges_and_items.sort();
    let should_print_debug_messages = ranges_and_items.ranges.len() <= 10;
    if should_print_debug_messages {
        println!("ranges: {:?}", ranges_and_items.ranges);
    }
    let ranges = ranges_and_items.ranges;
    let mut res: i64 = 0;
    let mut idx = 0;
    let m = ranges.len();
    while idx < m {
        let start_idx = idx;
        let range_start = ranges[idx][0];
        let mut range_end = ranges[idx][1];
        while idx + 1 < m && ranges[idx+1][0] <= range_end + 1 {
            idx += 1;
            range_end = ranges[idx][1].max(range_end);
        }
        if should_print_debug_messages {
            println!("start_idx = {}, idx = {}", start_idx, idx);
            print!("ranges = [");
            for r in &ranges[start_idx..idx+1] {
                print!("{:?}, ", r);
            }
            println!("]");
            println!("range_start = {}, range_end = {}", range_start, range_end);
        }
        res += range_end - range_start + 1;
        idx += 1;
    }
    res
}

fn test_part_b() -> bool {
    let ranges_and_items = RangesAndItems{
        ranges: vec![
            vec![1,2],
            vec![3,4],
            vec![11,15],
            vec![12,16],
            vec![13,17],
            vec![21,29],
            vec![22,23],
            vec![25,27],
            vec![31,35],
            vec![33,38],
            vec![37,39]
        ],
        items: vec![0;0],
    };
    let expected = 29;
    let actual = part_b(ranges_and_items);
    if actual != expected {
        println!("expected {}, got {}", expected, actual);
        return false;
    }
    true
}