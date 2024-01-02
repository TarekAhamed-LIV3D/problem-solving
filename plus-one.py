def increment(digits):
    i = len(digits) - 1

    while i >= 0:
        digits[i] += 1

        if digits[i] == 10:
            digits[i] = 0
        else:
            break
        i -= 1

    if i < 0 and digits[0] == 0:
        digits.insert(0, 1)
    return digits

large_integer = [9, 9, 9]
result = increment(large_integer)
print("Result after incrementing:", result)