class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned_s == cleaned_s[::-1]

input_string = "A man, a plan, a canal, Panama"

solution = Solution()
result = solution.isPalindrome(input_string)

print("Is the string a palindrome?", result)
