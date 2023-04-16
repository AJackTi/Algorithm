def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    ans=[]
    for i in candies:
        if i+extraCandies >= max(candies):
            ans.append(True)
        else:
            ans.append(False)

    return ans

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))