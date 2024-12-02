use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn safe(set: Vec<i32>) -> bool {
    let mut diffs = vec![];
    for (a, b) in set.iter().zip(set.iter().skip(1)) {
        diffs.push(a-b);
    }
    if diffs.iter().all(|&x| 1 <= x && x <= 3) || diffs.iter().all(|&x| -1 >= x && x >= -3) {
        return true;
    }
    false
}

fn main() -> std::io::Result<()> {
    if env::args().len() < 2 {
        println!("Wrong args");
        return Ok(());
    }
    let file = File::open(env::args().nth(1).unwrap())?;
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents)?;
    let lines = contents.split("\n").filter(|line| *line != "");
    let mut count: i32 = 0;
    for line in lines {
        let set: Vec<i32> = line
            .split(" ")
            .filter_map(|s| s.parse::<i32>().ok())
            .collect();
        //if safe(set) {
        //    count += 1;
        //}
        for i in 0..set.len() {
            let mut test_set: Vec<i32> = vec![];
            for j in 0..set.len() {
                if i == j {
                    continue;
                }
                test_set.push(set[j]);
            }
            if safe(test_set) {
                count += 1;
                break ;
            }
        }
    }
    println!("Total count: {}", count);
    Ok(())
}
