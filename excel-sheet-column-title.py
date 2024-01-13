class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result
            columnNumber //= 26
        
        return result

column_number = 701
solution = Solution()
result = solution.convertToTitle(column_number)

print(f"Column title for column number {column_number}: {result}")
