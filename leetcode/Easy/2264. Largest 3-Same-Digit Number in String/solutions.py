def largestGoodInteger(num: str) -> str:
    max_digit, current_digit, count = -1, num[0], 1

    for idx in range(1, len(num)):
        if current_digit == num[idx]:
            count += 1
            if count == 3 and int(num[idx]) > max_digit:
                max_digit, count = int(num[idx]), 0
        else:
            count = 1
            current_digit = num[idx]

    return str(max_digit) * 3 if max_digit != -1 else ""
        
print(largestGoodInteger("222"))