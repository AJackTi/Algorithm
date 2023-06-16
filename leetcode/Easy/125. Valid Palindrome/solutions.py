import re

def isPalindrome(s: str) -> bool:
    def isPalindrome(s):
        return s == s[::-1]
    
    s = re.sub(r'[\W_]', '', s).lower()
    return isPalindrome(s)

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s=s))