class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result

column_title = "AB"
solution = Solution()
result = solution.titleToNumber(column_title)

print(f"Column number for column title {column_title}: {result}")
