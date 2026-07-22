class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        cnt = Counter(s)

        for c in cnt:
            if cnt[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))

        return len(s)