class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def isPal(s):
            return s == s[::-1]

        mp = {word: i for i, word in enumerate(words)}
        ans = []

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                if isPal(prefix):
                    rev = suffix[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([mp[rev], i])

                if j != n and isPal(suffix):
                    rev = prefix[::-1]
                    if rev in mp and mp[rev] != i:
                        ans.append([i, mp[rev]])

        return ans