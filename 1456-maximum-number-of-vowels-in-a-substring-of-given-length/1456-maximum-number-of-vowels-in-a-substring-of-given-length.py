class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = ans = 0

        for i, c in enumerate(s):
            if c in "aeiou":
                count += 1
            if i >= k and s[i - k] in "aeiou":
                count -= 1
            if i >= k - 1:
                ans = max(ans, count)

        return ans