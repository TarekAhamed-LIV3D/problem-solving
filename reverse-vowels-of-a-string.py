def reverseVowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left].lower() not in vowels:
            left += 1

        while left < right and s[right].lower() not in vowels:
            right -= 1

        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)

input_str = "hello"
output_str = reverseVowels(input_str)
print(output_str)