from src.leetcode.arrs.PascalTriangle import PascalTriangle


class PascalTriangleTest:
    def testTenerate(self) -> None:
        assert [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ] == PascalTriangle.generate(5)
        assert [[1]] == PascalTriangle.generate(1)
