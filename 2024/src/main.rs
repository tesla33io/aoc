use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::env;

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
        let set: Vec<i32> = line.split(" ")
            .filter_map(|s| s.parse::<i32>().ok())
            .collect();
        let mut asorted: Vec<i32> = set.clone();
        asorted.sort();
        let mut dsorted: Vec<i32> = asorted.clone();
        dsorted.reverse();
        if set == asorted || set == dsorted {
            let diffs: Vec<i32> = set
                .windows(2)
                .map(|w| (w[1] - w[0]).abs())
                .collect();

            let sdiff = diffs.iter().min().unwrap();
            let ldiff = diffs.iter().max().unwrap();
            if *sdiff >= 1 && *ldiff <= 3 {
                // println!("...{:?}", set);
                // println!(" ..{:?}", asorted);
                // println!("  .{:?}", dsorted);
                count += 1;
            }
        }
    }
    println!("Total count: {}", count);
    Ok(())
}
