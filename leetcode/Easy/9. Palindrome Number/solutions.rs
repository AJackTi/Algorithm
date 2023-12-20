// fn is_palindrome(x: i32) -> bool {
//     x.to_string() == x.to_string().chars().rev().collect::<String>()
// }

fn is_palindrome(x: i32) -> bool {
    if x < 0 || (x % 10 == 0 && x != 0) {
        return false;
    }

    let mut reverse_number: i32 = 0;
    let mut temp_number: i32 = x;
    loop {
        if temp_number <= 0 {
            break;
        }
        reverse_number = reverse_number * 10 + (temp_number % 10);
        temp_number = temp_number / 10;
    }

    return reverse_number == x;
}

fn main() {
    let x = 121;
    println!("{}", is_palindrome(x));
}
