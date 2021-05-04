from typing import List


class TwoSum:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

    @staticmethod
    def two_sum2(nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i, num in enumerate(nums):
            if target - num in mapper:
                return [mapper[target - num], i]
            mapper[num] = i
        return [-1, -1]
