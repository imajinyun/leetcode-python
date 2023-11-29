from typing import List


class ThreeSum:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        if n < 3:
            return ans

        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] < nums[l + 1]:
                        l += 1
                    while l < r and nums[r] < nums[r + 1]:
                        r -= 1
                    l, r = l - 1, r - 1
        return ans
