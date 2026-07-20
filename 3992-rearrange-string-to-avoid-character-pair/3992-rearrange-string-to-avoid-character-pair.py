class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        cy = s.count(y)
        cx = s.count(x)

        ans = [y] * cy

        for ch in s:
            if ch != x and ch != y:
                ans.append(ch)

        ans.extend([x] * cx)
        return "".join(ans)