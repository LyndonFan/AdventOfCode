// use std::env;
use std::fs;

fn main() {
    if !test_sum_twice_numbers() {
        return;
    }
    if !test_is_number_repeating() {
        return;
    }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(test_input) = {}", test_input.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 1227775554", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 4174379265", test_res);

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
    let lines: Vec<&str> = contents.trim_end().split(',').collect();
    let mut res: Vec<Vec<i64>> = vec![vec![0;2]; lines.len()];
    for i in 0..lines.len() {
        let parts: Vec<_> = lines[i].split('-').collect();
        res[i][0] = parts[0].parse::<i64>().unwrap();
        res[i][1] = parts[1].parse::<i64>().unwrap();
    }
    res
}

fn generate_twice_numbers_for_n_digits(n: usize) -> Vec<i64> {
    let mut pow10 = 1;
    for _ in 0..n {
        pow10 *= 10;
    }
    let mut numbers = vec![0; pow10+1];
    pow10 = 1;
    for _ in 0..n {
        for i in pow10..10*pow10 {
            numbers[i] = (i*(10*pow10+1)) as i64;
        }
        pow10 *= 10;
    }
    numbers
}

fn test_sum_twice_numbers() -> bool {
    let n = 5;
    let numbers = generate_twice_numbers_for_n_digits(n);
    let test_cases = [[5,55],[43,4343],[314,314314],[9023,90239023],[23478,23478]];
    for i in 0..n {
        if test_cases.len() >= i {
            return true;
        }
        let index = test_cases[i][0];
        let expected = test_cases[i][1];
        let actual = numbers[index];
        if actual != (expected as i64) {
            println!("expected numbers[{}] = {}, got {}", index, expected, actual);
            return false;
        }
    }
    true
}

fn part_a(lines: Vec<Vec<i64>>) -> i64 {
    let mut res = 0;
    let numbers = generate_twice_numbers_for_n_digits(6);
    for iter_index in 0..lines.len() {
        let start = lines[iter_index][0];
        let end = lines[iter_index][1];
        let mut index = 0;
        while index < numbers.len() && numbers[index] < start {
            index += 1;
        }
        if index == numbers.len() {
            // println!("start = {}, end = {}, can't find repeat number larger than start", start, end);
            continue;
        }
        let mut s = 0;
        while index < numbers.len() && numbers[index] <= end {
            s += numbers[index];
            index += 1;
        }
        res += s;
        // println!("start = {}, end = {}, s = {}, res = {}", start, end, s, res);
    }
    res
}

// just noticed the actual ranges are quite small
// would be quicker to iterate over the ranges
// and check if each number in the range is repeating

fn is_number_repeating(n: i64) -> bool {
    if n <= 10 {
        return false;
    }
    let mut y = n;
    let mut num_digits = 0;
    while y > 0 {
        y /= 10;
        num_digits += 1;
    }
    let mut pow10 = 1;
    for i in 1..=num_digits/2 {
        pow10 *= 10;
        if num_digits%i != 0 {
            continue;
        }
        let back = n%pow10;
        let mut x = n/pow10;
        let mut is_repeating = true;
        while x > 0 && is_repeating {
            is_repeating = x%pow10 == back;
            x /= pow10;
        }
        if is_repeating {
            return true;
        }
    }
    false
}

fn test_is_number_repeating() -> bool {
    let passes = vec![11,9090,123123,111,242424,789789789,66666];
    for x in passes.iter() {
        if !is_number_repeating(*x) {
            println!("expected {} to be repeating", x);
            return false;
        }
    }
    let fails = vec![0,1,12,8090,23123,211,1242424,90090,76666666];
    for x in fails.iter() {
        if is_number_repeating(*x) {
            println!("expected {} to be not repeating", x);
            return false;
        }
    }
    true
}

fn part_b(lines: Vec<Vec<i64>>) -> i64 {
    let mut res = 0;
    for iter_index in 0..lines.len() {
        let start = lines[iter_index][0];
        let end = lines[iter_index][1];
        for n in start..=end {
            if is_number_repeating(n) {
                // println!("found {} repeating", n);
                res += n;
            }
        }
    }
    res
}
