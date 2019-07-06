import unittest
from main import Solution

obj = Solution()


class MatrixTests(unittest.TestCase):

    def test_1(self):
        """modifies input matrix."""
        input_matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        obj.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[0, 0, 0, 0], [
                         0, 4, 5, 0], [0, 3, 1, 0]])

    def test_2(self):
        """works"""
        input_matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        obj.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[0, 0, 0, 0], [
                         0, 4, 5, 0], [0, 3, 1, 0]])

        input_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        obj.setZeroes(input_matrix)
        self.assertEqual(input_matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])


if __name__ == '__main__':
    unittest.main()
