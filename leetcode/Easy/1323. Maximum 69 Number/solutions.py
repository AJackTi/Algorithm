def lenDigits(self, x: int) -> int: 
    """
    Assumes int(x)
    """

    x = abs(x)

    if x < 10:
        return 1

    return 1 + self.lenDigits(x / 10)

def sumPow(self, i: int) -> int:
    sum_num = 1
    while i > 0:
        sum_num += 10 ** i
        i -= 1
    return sum_num

def maximum69Number(self, num: int) -> int:
    len_digits = self.lenDigits(num)

    max_number = num
    len_digits -= 1
    count = 0
    while len_digits >= 0:
        if num // 10 ** len_digits < 9 * self.sumPow(count):
            return 9 * self.sumPow(count) * 10 ** len_digits + num % 10 ** len_digits
        len_digits -= 1
        count += 1
        
    return max_number