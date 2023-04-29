def largestAltitude(gain: list[int]) -> int:
    count, highest = 0, 0
    
    for i in gain :
        count += i
        
        if count > highest:
            highest = count
            
    return highest

gain = [-5,1,5,0,-7]
print(largestAltitude(gain=gain))