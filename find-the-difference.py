def findTheDifference(s, t):
    xor_result = 0
    for char in s + t:
        xor_result ^= ord(char)

    return chr(xor_result)

s = "abcd"
t = "abcde"
result = findTheDifference(s, t)

print(f"The added letter is: {result}")