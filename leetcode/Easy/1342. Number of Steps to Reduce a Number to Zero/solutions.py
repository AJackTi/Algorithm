def numberOfSteps(num: int) -> int:
    if num == 0:
        return 0
    count = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1

    return count

num = 14
print(numberOfSteps(num))