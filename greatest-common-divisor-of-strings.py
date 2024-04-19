#For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times). 
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

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