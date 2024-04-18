#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string. #

def merge_alternately(word1:str, word2:str) -> str:
    merged_word = ""
    max_length = max(len(word1), len(word2))

    for i in range(max_length):
        if i < len(word1):
            merged_word += word1[i]
        if i < len(word2):
            merged_word += word2[i]
    return merged_word

word1 = "abc"
word2 = "pqr"
merged_word = merge_alternately(word1, word2)
print(merged_word)