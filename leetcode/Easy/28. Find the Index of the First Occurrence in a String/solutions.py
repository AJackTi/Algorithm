def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)