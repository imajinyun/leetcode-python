from typing import List


class TwoSum:
    """[0001. Two Sum](https://leetcode.com/problems/two-sum/)"""

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        ans, cnt = [-1, -1], len(nums)
        if cnt <= 0:
            return ans

        for i, num in enumerate(nums):
            tmp = False
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    ans, tmp = [i, j], True
                    break
            if tmp:
                break
        return ans
