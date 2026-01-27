// use std::env;
use std::fs;
use std::collections::{HashMap};

fn main() {
    // println!("testing internal functions");
    // let passed_tests = test_part_b();
    // if !passed_tests {
    //     return;
    // }

    println!("Reading test.txt");
    let test_contents = fs::read_to_string("test.txt").expect("Should have been able to read test file");
    let test_input = parse(&test_contents);
    println!("len(input) = {}", test_input.rows.len());
    let mut test_res = part_a(test_input.clone());
    println!("Part a test res: {}, expect 40", test_res);
    test_res = part_b(test_input.clone());
    println!("Part b test res: {}, expect 25272", test_res);

    println!("Reading input.txt");
    let live_contents = fs::read_to_string("input.txt").expect("Should have been able to read input file");
    let live_input = parse(&live_contents);
    println!("len(input) = {}", live_input.rows.len());
    let mut live_res = part_a(live_input.clone());
    println!("Part a live res: {}", live_res);
    live_res = part_b(live_input.clone());
    println!("Part b live res: {}", live_res);
}

#[derive(Clone)]
struct Input {
    rows: Vec<Vec<i64>>,
    num_connections: i64,
}

fn parse(contents: &String) -> Input {
    let lines: Vec<_> = contents.trim().split("\n").collect();
    let rows: Vec<Vec<_>> = lines.iter().map(
        |x| x.split(",").map(
            |w| w.parse::<i64>().unwrap()
        ).collect()
    ).collect();
    let mut num_connections = 1000;
    if rows.len() < 100 {
        num_connections = 10;
    }
    Input{rows, num_connections}
}

struct DisjointForestSet {
    n: usize,
    parents: Vec<usize>,
    ranks: Vec<usize>,
    _num_sets: usize,
}

impl DisjointForestSet {
    pub fn new(n: usize) -> Self {
        Self{
            n: n,
            parents: (0..n).collect::<Vec<_>>(),
            ranks: vec![0; n],
            _num_sets: n,
        }
    }

    pub fn parent(&mut self, i: usize) -> usize {
        while self.parents[i] != self.parents[self.parents[i]] {
            self.parents[i] = self.parents[self.parents[i]];
        }
        self.parents[i]
    }

    pub fn join(&mut self, i: usize, j: usize) -> bool {
        let u = self.parent(i);
        let v = self.parent(j);
        if u == v {
            return false;
        };
        if self.ranks[u] <= self.ranks[v] {
            if self.ranks[u] == self.ranks[v] {
                self.ranks[v] += 1;
            }
            self.parents[v] = u;
            self.parents[j] = u;
        } else {
            self.parents[u] = v;
            self.parents[i] = v;
        };
        self._num_sets -= 1;
        true
    }

    pub fn num_sets(&self) -> usize {
        self._num_sets
    }

    pub fn all_parents(&mut self) -> Vec<usize> {
        for i in 0..self.n {
            self.parent(i);
        }
        self.parents.clone()
    }
}

fn squared_distance(point_a: &Vec<i64>, point_b: &Vec<i64>) -> i64 {
    let d = point_a.len();
    let mut res = 0;
    for i in 0..d {
        res += (point_a[i]-point_b[i])*(point_a[i]-point_b[i]);
    }
    res
}

fn part_a(parts: Input) -> i64 {
    let rows = parts.rows;
    let num_connections = parts.num_connections as usize;
    let n = rows.len();
    let print_debug_messages = n <= 20;
    let mut pairs: Vec<Vec<i64>> = vec![vec![0;3]; n*(n-1)/2];
    for (j, row_a) in rows.iter().enumerate() {
        for i in 0..j {
            let row_b = &rows[i];
            pairs[i + j*(j-1)/2] = vec![
                i as i64,
                j as i64,
                squared_distance(row_a,row_b),
            ];
        }
    }
    if print_debug_messages {
        println!("created pairs");
        println!("{:#?}", pairs);
    }
    pairs.sort_by(|va, vb| va[2].cmp(&vb[2]));
    let mut forest = DisjointForestSet::new(n);
    for idx in 0..num_connections {
        let xs = &pairs[idx];

        forest.join(xs[0] as usize, xs[1] as usize);
    }
    let mut parent_counts: HashMap<usize, usize> = HashMap::new();
    let parents = forest.all_parents();
    if print_debug_messages {
        println!("parents: {:#?}", parents);
    }
    for p in forest.all_parents() {
        parent_counts.entry(p).and_modify(|x| *x += 1).or_insert(1);
    }
    let mut sizes = Vec::with_capacity(parent_counts.len());
    for (_parent, count) in &parent_counts {
        sizes.push(count);
    }
    sizes.sort();
    sizes.reverse();
    println!("{}, {}, {}", sizes[0], sizes[1], sizes[2]);
    let mut res = 1;
    for i in 0..3 {
        res *= sizes[i];
    }
    res as i64
}

fn part_b(parts: Input) -> i64 {
    let rows = parts.rows;
    let n = rows.len();
    let print_debug_messages = n <= 20;
    let mut pairs: Vec<Vec<i64>> = vec![vec![0;3]; n*(n-1)/2];
    for (j, row_a) in rows.iter().enumerate() {
        for i in 0..j {
            let row_b = &rows[i];
            pairs[i + j*(j-1)/2] = vec![
                i as i64,
                j as i64,
                squared_distance(row_a,row_b),
            ];
        }
    }
    if print_debug_messages {
        println!("created pairs");
        println!("{:#?}", pairs);
    }
    pairs.sort_by(|va, vb| va[2].cmp(&vb[2]));
    let mut forest = DisjointForestSet::new(n);
    for xs in pairs {
        let joined = forest.join(xs[0] as usize, xs[1] as usize);
        if joined && forest.num_sets() == 1 {
            return rows[xs[0] as usize][0] * rows[xs[1] as usize][0];
        }
    }
    println!("reached end of loop without connecting all boxes!?");
    return 0;
}
