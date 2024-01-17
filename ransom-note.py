def canConstruct(ransomNote, magazine):
    char_count_ransomNote = {}
    char_count_magazine = {}

    for char in ransomNote:
        char_count_ransomNote[char] = char_count_ransomNote.get(char, 0) + 1

    for char in magazine:
        char_count_magazine[char] = char_count_magazine.get(char, 0) + 1

    for char, count in char_count_ransomNote.items():
        if char_count_magazine.get(char, 0) < count:
            return False

    return True

ransomNote = "aa"
magazine = "aab"
result = canConstruct(ransomNote, magazine)

print(f"Can construct ransomNote: {result}")