myList = [1,2,4,5,6,7,8,9,10]

def findMissing(list, n):
    sum1 = n*(n+1)/2
    sum2 = sum(list)
    return sum1-sum2

print(findMissing(myList, 10))