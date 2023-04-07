def plusOne(digits: list[int]) -> list[int]:
    digit_length = len(digits)
        
    i = digit_length - 1
    
    while digits[i] == 9 and i >= 0:
        i -= 1
    
    if i == -1:
        results = [0]*(digit_length + 1)
        results[0] = 1
        return results
    
    results = [0]*(digit_length)
    
    results[i] = digits[i] + 1
    
    for j in range(i-1, -1, -1):
        results[j] = digits[j]
    
    return results

# input = [9]
# input = [9,9]
# input = [1,2,3]
# input = [9,8,7,6,5,4,3,2,1,0]
input = [9,8,9]
output = plusOne(input)
print(output)