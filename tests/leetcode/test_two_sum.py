import pytest

from src.leetcode.TwoSum import TwoSum


class TestTwoSum:
    def test_two_sum(self) -> None:
        assert [0, 1] == TwoSum.two_sum([2, 7, 11, 15], 9)
        assert [-1, -1] == TwoSum.two_sum([2, 7, 11, 15], 10)

    def test_two_sum2(self) -> None:
        assert [0, 1] == TwoSum.two_sum2([2, 7, 11, 15], 9)
        assert [-1, -1] == TwoSum.two_sum2([2, 7, 11, 15], 10)
