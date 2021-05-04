from typing import List


class UnionFind:
    def __init__(self, grid: List[List[str]]):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            if self.rank[a] > self.rank[b]:
                self.parent[b] = a
            elif self.rank[a] < self.rank[b]:
                self.parent[a] = b
            else:
                self.parent[b] = a
                self.rank[a] += 1
            self.count -= 1
