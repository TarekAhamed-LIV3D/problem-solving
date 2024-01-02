def strStr(haystack, needle):
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

haystack = "hello"
needle = "ll"
result = strStr(haystack, needle)
print("Index of the first occurrence of", needle, "in", haystack, ":", result)