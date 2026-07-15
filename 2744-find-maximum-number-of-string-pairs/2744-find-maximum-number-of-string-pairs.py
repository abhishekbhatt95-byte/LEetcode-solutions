class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        ans = 0

        for word in words:
            if word[::-1] in s:
                ans += 1
            s.add(word)

        return ans