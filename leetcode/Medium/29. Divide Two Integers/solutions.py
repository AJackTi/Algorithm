import math

def divide(dividend: int, divisor: int) -> int:
    result = math.trunc(dividend / divisor)
    if result >= 2147483648:
        return 2147483647
    return result