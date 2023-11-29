from typing import List


class PascalTriangle:
    """[0118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)"""

    @staticmethod
    def generate(n: int) -> List[List[int]]:
        ans = []
        if n <= 0:
            return ans

        ans = [[1] * (i + 1) for i in range(n)]
        for i in range(n):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans
