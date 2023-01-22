def sumOfDigits(n):
    assert n >= 0 and int(
        n) == n, 'The number has to be a positive integer only!'
    if n == 0:
        return 0
    return int(n % 10) + sumOfDigits(int(n/10))


def power(base, exp):
    assert exp >= 0 and int(
        exp) == exp, 'The exponent must be positive integer only'
    if exp == 0:
        return 0
    if exp == 1:
        return base
    return base * power(base, exp - 1)


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b == 0:
        return a
    return gcd(b, int(a % b))


def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only!'
    if n == 0:
        return 0
    return n % 2 + 10 * decimalToBinary(int(n/2))

# print(sumOfDigits(10))
# print(sumOfDigits(11))
# print(sumOfDigits(123))
# print(sumOfDigits(1456))

# print(power(2, 4))
# print(power(2, 1))
# print(power(2, -1))
# print(power(2, 1.1))
# print(power(2, 0))


# print(gcd(8, 12))


# print(decimalToBinary(13))
