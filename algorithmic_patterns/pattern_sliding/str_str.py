def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if not haystack:
        return - 1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


# print(strStr("", ""))
# print(strStr("a", ""))
# print(strStr("", "a"))
print(strStr("mississippi", "pi"))
