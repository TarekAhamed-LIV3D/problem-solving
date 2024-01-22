class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, max_len = 0, 1

        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)

            current_max_len = max(len1, len2)
            if current_max_len > max_len:
                start = i - (current_max_len - 1) // 2
                max_len = current_max_len

        return s[start:start + max_len]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

solution = Solution()
s1 = "babad"
s2 = "cbbd"

print(solution.longestPalindrome(s1))
print(solution.longestPalindrome(s2))