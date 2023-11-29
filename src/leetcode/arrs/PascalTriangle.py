from typing import List


class PascalTriangle:
    """[0118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)"""

    @staticmethod
    def generate(n: int) -> List[List[int]]:
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
