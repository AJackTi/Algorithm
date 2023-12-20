fn two_sum(nums: Vec<i32>, target: i32) -> (i32, i32) {
    let mut map = std::collections::HashMap::new();
    for (i, num) in nums.iter().enumerate() {
        if let Some(j) = map.get(&(target - num)) {
            return (*j as i32, i as i32);
        }
        map.insert(num, i);
    }

    return (0, 0);
}

fn main() {
    let (val, idx) = two_sum(vec![3, 2, 4], 6);
    println!("{val} {idx}");
    let (val, idx) = two_sum(vec![3, 2, 4], 5);
    println!("{val} {idx}");
    let (val, idx) = two_sum(vec![0, 4, 3, 0], 5);
    println!("{val} {idx}");
    let (val, idx) = two_sum(vec![0, 1], 1);
    println!("{val} {idx}");
}
