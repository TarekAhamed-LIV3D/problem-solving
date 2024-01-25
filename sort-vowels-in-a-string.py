def permuteString(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    consonants = [c for c in s if c not in vowels]
    vowels_sorted = sorted([c for c in s if c in vowels])

    result = []
    consonant_idx = 0
    vowel_idx = 0

    for char in s:
        if char in vowels:
            result.append(vowels_sorted[vowel_idx])
            vowel_idx += 1
        else:
            result.append(consonants[consonant_idx])
            consonant_idx += 1

    return ''.join(result)

s = "leetcode"
print(permuteString(s))