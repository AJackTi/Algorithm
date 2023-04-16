import sys

def shortestToChar(s: str, c: str) -> list[int]:
    c_indexes = [i for i in range(len(s)) if s[i] == c]
            
    results = []    
    for i, s_c in enumerate(s):
        min_distance = sys.maxsize
        for c_i in c_indexes:
            min_distance = min(abs(i - c_i), min_distance)
                            
        results.append(min_distance)
                
    return results

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))