def lengthOfLastWord(s):
    words = s.split()

    if not words:
        return 0

    return len(words[-1])

input_string = "Hello World"
result = lengthOfLastWord(input_string)
print("Length of the last word:", result)
