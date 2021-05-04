import unittest

from src.leetcode.TwoSum import TwoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self) -> None:
        self.assertEqual([0, 1], TwoSum.two_sum([2, 7, 11, 15], 9))
        self.assertEqual([-1, -1], TwoSum.two_sum([2, 7, 11, 15], 10))

    def test_two_sum2(self) -> None:
        self.assertEqual([0, 1], TwoSum.two_sum2([2, 7, 11, 15], 9))
        self.assertEqual([-1, -1], TwoSum.two_sum2([2, 7, 11, 15], 10))


if __name__ == '__main__':
    unittest.main()
