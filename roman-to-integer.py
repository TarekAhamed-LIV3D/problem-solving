def roman_to_int(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in s:
        value = roman_values[char]
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total

roman_numeral = "MCMXCIVIV"
result = roman_to_int(roman_numeral)
print(result)
