from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1

        for num, freq in cnt.items():
            if num == freq:
                ans = max(ans, num)

        return ans