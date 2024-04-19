def gcdOfStrings(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    g = gcd(len1, len2)
    
    substr = str1[:g]
    
    if substr * (len1 // g) == str1 and substr * (len2 // g) == str2:
        return substr
    else:
        return ""
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

str1 = "ABCABC"
str2 = "ABC"
result = gcdOfStrings(str1, str2)
print(result)