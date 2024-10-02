class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        x = len(word1)
        y = len(word2)
        if  x != y:
            return False
        else:
            c1 = {}
            c2 = {}
            for char in word1:
                if char in c1:
                    c1[char] += 1
                else:
                    c1[char] = 1
            for char in word2:
                if char in c2:
                    c2[char] += 1
                else:
                    c2[char] = 1
            w = sorted(c1.values())
            x = sorted(c2.values())
            y = set(word1)
            z = set(word2)
            if  w == x and y == z:
                return True
            else:
                return False

word1 = "cabbba"
word2 = "abbccc"
Solution = Solution()
ans = Solution.closeStrings(word1, word2)
print(ans)