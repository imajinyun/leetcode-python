from typing import List


class TwoSum:
    """0001. (Two Sum)[https://leetcode.com/problems/two-sum/]"""

    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i, numi in enumerate(nums):
            for j, numj in enumerate(range(i + 1, len(nums))):
                if numi + numj == target:
                    return [j, i]
        return [-1, -1]

    @staticmethod
    def two_sum2(nums: List[int], target: int) -> List[int]:
        mps = {}
        for i, num in enumerate(nums):
            if target - num in mps:
                return [mps[target - num], i]
            mps[num] = i
        return [-1, -1]
