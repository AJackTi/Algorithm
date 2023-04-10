def countDigits(num: int) -> int:
    temp = num
    count = 0
    while num > 0:
        remainder = num % 10
        if temp % remainder == 0:
            count += 1
        num = num // 10
    
    return count

print(countDigits(54))