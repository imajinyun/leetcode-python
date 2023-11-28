from typing import List


class PascalTriangle:
    @staticmethod
    def generate(n: int) -> List[List[int]]:
        """Array"""
        ans = []
        if n <= 0:
            return ans

        for i in range(n):
            rows = []
            for j in range(i + 1):
                if j in (0, i):
                    rows.append(1)
                else:
                    last = ans[i - 1]
                    rows.append(last[j - 1] + last[j])
            ans.append(rows)
        return ans

    @staticmethod
    def generate2(n: int) -> List[List[int]]:
        """Hash Table"""
        ans = []
        if n <= 0:
            return ans

        ans = [[1] * (i + 1) for i in range(n)]
        for i in range(n):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans
