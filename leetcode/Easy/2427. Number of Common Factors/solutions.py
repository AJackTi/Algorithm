def commonFactors(a: int, b: int) -> int:
    less = min(a,b)
    count = 0
    for i in range(1, less//2 + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    
    if max(a,b) % less == 0:
        count += 1
    
    return count

a = 12
b = 6
print(commonFactors(a=a, b=b))