def reverseWords(s):
    words = s.split()
    
    reversed_words = words[::-1]
    
    result = ' '.join(reversed_words)
    return result

input_str = "  L 1 V 3 D  "
print(reverseWords(input_str))