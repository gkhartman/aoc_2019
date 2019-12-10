/*  AOC Day 1
 *  Read an input list of mass values, perform a set of operations and
 *  add the result to a running total.
 *
 *  Solutions to Part 1 and Part 2.
 */

use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn get_req_fule(mass: i32) -> i32 {
    return mass / 3 - 2;
}

fn get_recursive_fule(mass: i32) -> i32 {
    let rfule: i32 = get_req_fule(mass);
    if rfule > 0 {
        return rfule + get_recursive_fule(rfule);
    }
    return 0;
}

fn part1() -> i32 {
    let mut total: i32 = 0;
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let mass_int: i32 = line.unwrap().parse::<i32>().unwrap();
        total += get_req_fule(mass_int);
    }
    return total;
}

fn part2() -> i32 {
    let mut total: i32 = 0;
    let file = File::open("input.txt").unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let mass_int: i32 = line.unwrap().parse::<i32>().unwrap();
        let init_fule:i32 = get_req_fule(mass_int);
        total += init_fule + get_recursive_fule(init_fule);
    }

    return total;
}

fn main() -> std::io::Result<()> {
    println!("Part 1: {}", part1());
    println!("Part 2: {}", part2());
    Ok(())
}
