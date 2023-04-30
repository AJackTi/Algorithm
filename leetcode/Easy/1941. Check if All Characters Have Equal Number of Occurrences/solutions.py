def areOccurrencesEqual(s: str) -> bool:
    first_element = s[0]
    occurrences = s.count(first_element)
    set_exclude_first_element = set(s) - set(first_element)
    for i in set_exclude_first_element:
        if s.count(i) != occurrences:
            return False
        
    return True

# s = "abacbc"
s = "aaabb"
print(areOccurrencesEqual(s=s))