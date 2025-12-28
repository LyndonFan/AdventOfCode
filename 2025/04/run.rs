// use std::env;
use std::fs;
use std::collections::VecDeque;
use std::io::{stdin, stdout, Write};

fn main() {
    println!("testing internal functions");
    let passed_tests = true;
    if !passed_tests {
        return;
    }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(test_input) = {}", test_input.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 13", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 43", test_res);

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
    let lines: Vec<&str> = contents.trim().split('\n').collect();
    lines
}

fn part_a(lines: Vec<&str>) -> i64 {
    let mut res = 0;
    let dirs = vec![
        vec![-1,-1],
        vec![-1,0],
        vec![-1,1],
        vec![0,-1],
        vec![0,1],
        vec![1,-1],
        vec![1,0],
        vec![1,1],
    ];
    let m = lines.len();
    let n = lines[0].len();
    let should_print_debug_messages = false;
    for i in 0..m {
        for j in 0..n {
            if lines[i].as_bytes()[j] != b'@' {
                continue;
            }
            let mut num_ats = 0;
            for ds in &dirs {
                if i == 0 && ds[0] == -1 {
                    continue;
                }
                if j == 0 && ds[1] == -1 {
                    continue;
                }
                let x = ((i as i64)+ds[0]) as usize;
                let y = ((j as i64)+ds[1]) as usize;
                if x>=m || y>=n {
                    continue;
                }
                if lines[x].as_bytes()[y] == b'@' {
                    num_ats += 1;
                }
            }
            if num_ats < 4 {
                if should_print_debug_messages {
                    println!("found okay at ({},{})", i, j);
                }
                res += 1;
            }
        }
    }
    res
}

fn part_b(lines: Vec<&str>) -> i64 {
    let mut res = 0;
    let dirs = vec![
        vec![-1,-1],
        vec![-1,0],
        vec![-1,1],
        vec![0,-1],
        vec![0,1],
        vec![1,-1],
        vec![1,0],
        vec![1,1],
    ];
    let m = lines.len();
    let n = lines[0].len();
    let mut bytes: Vec<Vec<u8>> = vec![Vec::new(); m];
    for i in 0..m {
        bytes[i] = lines[i].as_bytes().to_vec();
    }
    let mut queue = VecDeque::new();
    let mut processed = vec![vec![false; n]; m];
    let mut num_ats = vec![vec![0; n]; m];
    let should_print_debug_messages = false; // lines.len() <= 10;
    for i in 0..m {
        for j in 0..n {
            if bytes[i][j] != b'@' {
                continue;
            }
            let mut ct = 0;
            for ds in &dirs {
                if i == 0 && ds[0] == -1 {
                    continue;
                }
                if j == 0 && ds[1] == -1 {
                    continue;
                }
                let x = ((i as i64)+ds[0]) as usize;
                let y = ((j as i64)+ds[1]) as usize;
                if x>=m || y>=n {
                    continue;
                }
                if lines[x].as_bytes()[y] == b'@' {
                    ct += 1;
                }
            }
            num_ats[i][j] = ct;
            if ct < 4 {
                processed[i][j] = true;
                queue.push_back(vec![i,j]);
            }
        }
    }
    while queue.len() > 0 {
        res += 1;
        let i = queue[0][0];
        let j = queue[0][1];
        if should_print_debug_messages {
            print!("{}[2J", 27 as char);
            println!("processing ({},{})", i, j);
            print!("added");
        }
        bytes[i][j] = b'.';
        for ds in &dirs {
            if i == 0 && ds[0] == -1 {
                continue;
            }
            if j == 0 && ds[1] == -1 {
                continue;
            }
            let x = ((i as i64)+ds[0]) as usize;
            let y = ((j as i64)+ds[1]) as usize;
            if x>=m || y>=n {
                continue;
            }
            if bytes[x][y] != b'@' {
                continue;
            }
            num_ats[x][y] -= 1;
            if !processed[x][y] && num_ats[x][y] < 4 {
                processed[x][y] = true;
                queue.push_back(vec![x,y]);
                if should_print_debug_messages {
                    print!(" ({},{}),", x, y);
                }
            }
        }
        queue.pop_front();
        if should_print_debug_messages {
            println!("");
            println!("queue = {:?}", queue);
            for bs in &bytes {
                let s = str::from_utf8(&bs).unwrap();
                println!("{}", s);
            }
            // let mut user_input = String::new();
            // print!("Press q to quit, anything else to continue: ");
            // let _ = stdout().flush();
            // stdin().read_line(&mut user_input).expect("Did not enter a correct string");
            // user_input = user_input.trim().to_string();
            // if user_input == "q" {
            //     std::process::exit(0);
            // }
        }
    }
    if should_print_debug_messages {
        print!("{}[2J", 27 as char);
    }
    res
}
