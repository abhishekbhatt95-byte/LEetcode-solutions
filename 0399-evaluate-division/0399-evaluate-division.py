class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(src, dst, vis):
            if src == dst:
                return 1.0

            vis.add(src)
            for nei, val in graph[src]:
                if nei not in vis:
                    res = dfs(nei, dst, vis)
                    if res != -1:
                        return val * res
            return -1

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set()))

        return ans