from collections import defaultdict

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g):
            m, n = len(g), len(g[0])
            s1 = s2 = 0
            cnt1 = defaultdict(int)
            cnt2 = defaultdict(int)

            for row in g:
                for x in row:
                    s2 += x
                    cnt2[x] += 1

            for i, row in enumerate(g[:-1]):
                for x in row:
                    s1 += x
                    s2 -= x
                    cnt1[x] += 1
                    cnt2[x] -= 1

                if s1 == s2:
                    return True

                if s1 < s2:
                    d = s2 - s1
                    if cnt2[d]:
                        if ((m - i - 1 > 1 and n > 1) or
                            (i == m - 2 and (g[i + 1][0] == d or g[i + 1][-1] == d)) or
                            (n == 1 and (g[i + 1][0] == d or g[-1][0] == d))):
                            return True
                else:
                    d = s1 - s2
                    if cnt1[d]:
                        if ((i + 1 > 1 and n > 1) or
                            (i == 0 and (g[0][0] == d or g[0][-1] == d)) or
                            (n == 1 and (g[0][0] == d or g[i][0] == d))):
                            return True
            return False

        return check(grid) or check(list(map(list, zip(*grid))))