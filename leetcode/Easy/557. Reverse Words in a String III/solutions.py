def reverseWords(s: str) -> str:
    ans_lst = []
    for i in s.strip().split(' '):
        ans_lst.append(i[::-1])
    
    return ' '.join(ans_lst)

s = "Let's take LeetCode contest"
print(reverseWords(s=s))