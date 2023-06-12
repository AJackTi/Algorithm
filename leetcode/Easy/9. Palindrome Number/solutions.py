def isPalindrome(x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    
    reverse_number = 0
    temp_number = x
    while temp_number > 0:
        reverse_number = reverse_number * 10 + temp_number % 10
        temp_number //= 10
    
    return reverse_number == x

x = 121
print(isPalindrome(x=x))
