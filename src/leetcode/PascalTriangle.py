from typing import List


class PascalTriangle:
    @staticmethod
    def generate(n: int) -> List[List[int]]:
        ans = []
        if n <= 0:
            return ans
        for i in range(n):
            sub = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    sub.append(1)
                else:
                    last = ans[i - 1]
                    sub.append(last[j - 1] + last[j])
            ans.append(sub)
        return ans

    @staticmethod
    def generate2(n: int) -> List[List[int]]:
        if n <= 0:
            return []
        ans = [[1] * (i + 1) for i in range(n)]
        for i in range(n):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans
