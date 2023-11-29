from typing import List


class TwoSum:
    """[0001. Two Sum](https://leetcode.com/problems/two-sum/)"""

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        ans, cnt, mps = [], len(nums), {}
        if cnt <= 0:
            return ans
        for i, num in enumerate(nums):
            val = target - num
            if val in mps:
                ans = [mps[val], i]
                break
            mps[num] = i
        return ans
