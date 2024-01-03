def addBinary(a, b):
    len_a, len_b = len(a), len(b)
    max_len = max(len_a, len_b)

    a = '0' * (max_len - len_a) + a
    b = '0' * (max_len - len_b) + b

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    if carry:
        result = '1' + result

    return result

binary_a = "01101"
binary_b = "10111"
result = addBinary(binary_a, binary_b)
print("Sum of", binary_a, "and", binary_b, "in binary:", result)