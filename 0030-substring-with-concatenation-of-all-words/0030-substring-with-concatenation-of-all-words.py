from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        n = len(words)
        k = len(words[0])
        total = n * k
        target = Counter(words)
        ans = []

        for i in range(k):
            left = i
            count = 0
            seen = Counter()

            for j in range(i, len(s) - k + 1, k):
                word = s[j:j + k]

                if word in target:
                    seen[word] += 1
                    count += 1

                    while seen[word] > target[word]:
                        seen[s[left:left + k]] -= 1
                        left += k
                        count -= 1

                    if count == n:
                        ans.append(left)
                        seen[s[left:left + k]] -= 1
                        left += k
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = j + k

        return ans