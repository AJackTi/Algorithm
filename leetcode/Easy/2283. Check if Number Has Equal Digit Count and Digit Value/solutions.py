def digitCount(num: str) -> bool:
    for i in range(len(num)):
        if num.count(str(i)) != int(num[i]):
            return False
        
    return True

# num = "1210"
num = "030"
print(digitCount(num=num))