// use std::env;
use std::fs;

fn main() {
    println!("testing largest_number_from_line");
    let passed_tests = test_largest_number_from_line();
    if !passed_tests {
        return;
    }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(test_input) = {}", test_input.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 357", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 3121910778619", test_res);

    println!("Reading input.txt");
    let live_contents = fs::read_to_string("input.txt").expect("Should have been able to read input file");
    let live_input = parse(&live_contents);
    println!("len(live_input) = {}", live_input.len());
    let mut live_res = part_a(live_input.clone());
    println!("Part a live res: {}", live_res);
    live_res = part_b(live_input.clone());
    println!("Part b live res: {}", live_res);
}

fn parse(contents: &String) -> Vec<Vec<i64>> {
    let lines: Vec<&str> = contents.split('\n').collect();
    let mut res: Vec<Vec<i64>> = vec![Vec::new(); lines.len()-1];
    for i in 0..lines.len()-1 {
        res[i] = vec![0; lines[i].len()];
        for (j, c) in lines[i].char_indices() {
            res[i][j] = c as i64 - '0' as i64;
        }
    }
    res
}

fn part_a(lines: Vec<Vec<i64>>) -> i64 {
    let mut res = 0;
    for line in lines.iter() {
        let mut last_max = 0;
        let mut record = 0;
        let mut is_first_char = true;
        for curr in line.clone().into_iter().rev() {
            if is_first_char {
                is_first_char = false;
            } else if 10*curr + last_max > record {
                record = 10*curr + last_max;
            }
            if curr > last_max {
                last_max = curr;
            }
        }
        // if lines.len() < 10 {
        //     println!("line = {:?}, record = {}", line, record);
        // }
        res += record as i64;
    }
    res
}

fn largest_number_from_line(
    line: Vec<i64>,
    num_digits: usize
) -> i64 {
    let mut pow_10s = vec![0; num_digits];
    let mut curr_pow_10 = 1;
    for i in 0..num_digits {
        pow_10s[i] = curr_pow_10;
        curr_pow_10 *= 10;
    }

    let n = line.len();
    let mut prev_line = vec![0; num_digits];
    prev_line[0] = line[n-1];
    for line_idx in (0..n-1).rev() {
        let mut curr_line = vec![0; num_digits];
        let x = line[line_idx];
        if x > prev_line[0] {
            curr_line[0] = x;
        } else {
            curr_line[0] = prev_line[0];
        }
        for i in 1..num_digits {
            if prev_line[i-1] == 0 {
                continue;
            }
            let new_number = x*pow_10s[i] + prev_line[i-1];
            curr_line[i] = new_number.max(prev_line[i]);
        }
        prev_line = curr_line;
    }
    prev_line[num_digits-1]
}

struct TestCase {
    line: Vec<i64>,
    num_digits: usize,
    expected_answer: i64,
}

fn test_largest_number_from_line() -> bool {
    let test_cases = vec![
        TestCase{
            line: vec![9,1,1,4,2,3,4],
            num_digits: 3,
            expected_answer: 944
        },
        TestCase{
            line: vec![9, 8, 8, 2, 3, 4, 4, 2, 9, 2, 2, 3, 2, 7, 2, 2],
            num_digits: 12,
            expected_answer: 988492232722
        }
    ];
    for test_case in test_cases {
        println!("Running test case");
        println!("line: {:?}", &test_case.line);
        println!("num_digits: {:?}", test_case.num_digits);
        let actual = largest_number_from_line(test_case.line, test_case.num_digits);
        if actual != test_case.expected_answer {
            print_both(test_case.expected_answer, actual);
            return false;
        } else {
            println!("passed, got {}", actual);
        }
    }
    true
}

fn part_b(lines: Vec<Vec<i64>>) -> i64 {
    let mut res = 0;
    let num_digits = 12;
    for line in lines.iter() {
        let line_res = largest_number_from_line(line.to_vec(), num_digits);
        println!("line={:?}, line_res={}", line, line_res);
        res += line_res;
    }
    res
}

fn print_both(expected_number: i64, actual_number: i64) {
    let expected = expected_number.to_string();
    let actual = actual_number.to_string();
    let green = "\x1b[92m";
    let red = "\x1b[91m";
    let escape = "\x1b[0m";
    print!("Expected: ");
    for (e, a) in expected.chars().zip(actual.chars()) {
        if e == a {
            print!("{}", e);
        } else {
            print!("{}{}{}", green, e, escape);
        }
    }
    println!();
    print!("Actual:   ");
    for (e, a) in expected.chars().zip(actual.chars()) {
        if e == a {
            print!("{}", a);
        } else {
            print!("{}{}{}", red, a, escape);
        }
    }
    println!();
}
