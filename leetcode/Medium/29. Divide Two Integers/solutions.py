# import math

# def divide(dividend: int, divisor: int) -> int:
#     result = math.trunc(dividend / divisor)
#     if result >= 2147483648:
#         return 2147483647
#     return result

import math

MAX = 2147483648

def divide(dividend: int, divisor: int) -> int:
    if dividend == -1 * MAX and divisor == 1 or dividend == MAX and divisor == - 1:
            return dividend * divisor
    flag = False
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        flag = True
    
    dividend = abs(dividend)
    divisor = abs(divisor)

    if dividend == MAX and divisor == 1:
        return MAX - 1 if not flag else (MAX - 1) * -1

    result = 0
    while dividend >= divisor:
        shift = 0
        while dividend >= divisor<<shift:
            shift+=1

        result += (1<<(shift-1))
        dividend -= divisor<<(shift-1)
    
    if flag :
        result *= -1
    
    return result

print(divide(-2147483648, -1))