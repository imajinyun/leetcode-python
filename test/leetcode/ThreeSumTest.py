from src.leetcode.ThreeSum import ThreeSum


class ThreeSumTest:
    @staticmethod
    def testThreeSum() -> None:
        assert [
            [-6, 3, 3],
            [-4, 1, 3],
            [-1, -1, 2],
            [-1, 0, 1],
        ] == ThreeSum.threeSum([-1, 0, 1, 2, -1, -4, -6, 3, 3])
        assert [[-1, -1, 2], [-1, 0, 1]] == ThreeSum.threeSum([-1, 0, 1, 2, -1, -4])
        assert [] == ThreeSum.threeSum([0])
        assert [] == ThreeSum.threeSum([0, 1, 1])
        assert [0, 0, 0] == ThreeSum.threeSum([0, 0, 0])
