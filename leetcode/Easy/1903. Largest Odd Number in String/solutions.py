def largestOddNumber(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if num[i] in {'1', '3', '5', '7', '9'}:
            return num[:i + 1]
    return ''
    
# print(largestOddNumber("52"))
# print(largestOddNumber("4206"))
print(largestOddNumber("35427"))