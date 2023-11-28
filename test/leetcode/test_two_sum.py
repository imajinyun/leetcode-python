from src.leetcode.TwoSum import TwoSum


class TestTwoSum:
    @staticmethod
    def test_two_sum() -> None:
        assert [0, 1] == TwoSum.twoSum([2, 7, 11, 15], 9)
        assert [-1, -1] == TwoSum.twoSum([2, 7, 11, 15], 10)
        assert [0, 1] == TwoSum.twoSum([3, 3], 6)

    @staticmethod
    def test_two_sum2() -> None:
        assert [0, 1] == TwoSum.twoSum2([2, 7, 11, 15], 9)
        assert [-1, -1] == TwoSum.twoSum2([2, 7, 11, 15], 10)
        assert [0, 1] == TwoSum.twoSum2([3, 3], 6)
