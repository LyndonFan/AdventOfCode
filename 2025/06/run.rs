// use std::env;
use std::fs;

fn main() {
    // println!("testing internal functions");
    // let passed_tests = test_part_b();
    // if !passed_tests {
    //     return;
    // }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(input[0]) = {}", test_input[0].len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 4277556", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 3263827", test_res);

    println!("Reading input.txt");
    let live_contents = fs::read_to_string("input.txt").expect("Should have been able to read input file");
    let live_input = parse(&live_contents);
    println!("len(input[0]) = {}", live_input[0].len());
    let mut live_res = part_a(live_input.clone());
    println!("Part a live res: {}", live_res);
    live_res = part_b(live_input.clone());
    println!("Part b live res: {}", live_res);
}

fn parse(contents: &String) -> Vec<&str> {
    let parts: Vec<&str> = contents.trim().split("\n").collect();
    parts
}

fn part_a(parts: Vec<&str>) -> i64 {
    let mut res = 0;
    let should_print_debug_messages = parts[0].len() <= 10;
    let symbols: Vec<_> = parts[parts.len() - 1].split_whitespace().map(|s| s.to_string()).collect();
    let mut numbers: Vec<Vec<i64>> = Vec::new();
    for i in 0..parts.len()-1 {
        numbers.push(
            parts[i].split_whitespace().map(|s| s.parse::<i64>().unwrap()).collect()
        );
    }
    if should_print_debug_messages {
        for nums in numbers.clone().into_iter() {
            println!("{:?}", nums);
        }
        println!("{:?}", symbols);
    }
    let m = &numbers.len();
    let n = &numbers[0].len();
    for col_num in 0..*n {
        if symbols[col_num] == "+" {
            let mut x = 0;
            for row_num in 0..*m {
                x += numbers[row_num][col_num];
            }
            res += x;
        } else {
            let mut x = 1;
            for row_num in 0..*m {
                x *= numbers[row_num][col_num];
            }
            res += x;
        }
    }
    res
}

fn part_b(parts: Vec<&str>) -> i64 {
    let m = parts.len();
    let n = parts[0].len();
    let bytes: Vec<Vec<_>> = parts.into_iter().map(|x| x.bytes().collect::<Vec<_>>()).collect();
    let mut res = 0;
    let mut c = 0;
    let should_print_debug_messages = n <= 30;
    while c < n {
        let symbol = bytes[m-1][c];
        let mut nums: Vec<i64> = Vec::new();
        while c<n {
            let mut curr_num = 0;
            let mut has_number = false;
            for r in 0..m-1 {
                if bytes[r][c] == b' ' {
                    continue;
                }
                has_number = true;
                curr_num = 10*curr_num + ((bytes[r][c] - '0' as u8) as i64);
            }
            if !has_number {
                break;
            }
            nums.push(curr_num);
            c += 1;
        }
        let mut temp_res = 0;
        if symbol == b'+' {
            for x in nums.iter() {
                temp_res += x;
            }
        } else if symbol == b'*' {
            temp_res = 1;
            for x in nums.iter() {
                temp_res *= x;
            }
        }
        if should_print_debug_messages {
            println!("nums = {:?}", nums);
            println!("symbol = {}", symbol);
            println!("temp_res = {}", temp_res);
        }
        res += temp_res;
        c += 1;
    }
    res
}
