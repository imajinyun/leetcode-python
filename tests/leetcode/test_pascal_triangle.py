import pytest

from src.leetcode.PascalTriangle import PascalTriangle


class TestPascalTriangle:
    def test_generate(self) -> None:
        assert [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]] == PascalTriangle.generate(5)
        assert [[1]] == PascalTriangle.generate(1)

    def test_generate2(self) -> None:
        assert [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]] == PascalTriangle.generate2(5)
        assert [[1]] == PascalTriangle.generate2(1)
