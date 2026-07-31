from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        cnt = Counter(word)
        ans = 0

        for i, f in enumerate(sorted(cnt.values(), reverse=True)):
            ans += (i // 8 + 1) * f

        return ans