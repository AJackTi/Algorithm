def hammingDistance(x: int, y: int) -> int:
    result = x ^ y
    count = 0
    
    for i in format(result, '08b'):
        if i == '1':
            count += 1
            
    return count

x = 1
y = 4
print(hammingDistance(x, y))