from typing import List
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph, self.low, self.res = {n: [] for n in range(n)}, [0] * n, []

        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.dfs()

        return self.res

    def dfs(self, node=0, parent=-1, reachable=1) -> None:
        self.low[node] = reachable

        for neighbor in self.graph[node]:
            if neighbor != parent:
                if not self.low[neighbor]:
                    self.dfs(neighbor, node, reachable + 1)
                if self.low[neighbor] > reachable:
                    self.res.append([node, neighbor])
                else:
                    self.low[node] = min(self.low[node], self.low[neighbor])


sol = Solution()
print(sol.criticalConnections(n = 7, connections = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]))