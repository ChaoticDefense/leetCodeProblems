class Solution:
    def scoreOfString(self, s: str) -> int:
        # Initialize score value
        score = 0

        # Iterate over string to the (n-1) character
        # For each character, add up the absolute value difference of ASCII values
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))

        return score


str = "hello"
s = Solution()
print(s.scoreOfString(str))