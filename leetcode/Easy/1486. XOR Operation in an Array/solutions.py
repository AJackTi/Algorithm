def xorOperation(n: int, start: int) -> int:
    if n == 0: return 0
    
    result = 0
    
    for i in range(n):
        result ^= start + 2 * i
        
    return result

n = 4
start = 3
print(xorOperation(n, start))