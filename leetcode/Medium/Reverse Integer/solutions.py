def reverse(x: int) -> int:
    result = 0
    temp = x
    if x < 0:
        x *= -1
    while x > 0:
        remainder = int(x % 10)
        result = (result * 10) + remainder
        x=int(x/10)

    if temp < 0:
        result*=-1

    if result > 2**31 - 1:
        return 0

    if result < -2**31 - 1:
        return 0

    return result

print(reverse(123))