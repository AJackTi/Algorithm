import math

def numberOfMatches(n: int) -> int:
    matches = n//2
    team = n - matches
    ans = matches
    while team != 1:
        matches = (team // 2)
        team = team - team//2
        ans += matches

    return ans

print(numberOfMatches(3))