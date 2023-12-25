def is_palindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]

num = 121
result = is_palindrome(num)
print(result)