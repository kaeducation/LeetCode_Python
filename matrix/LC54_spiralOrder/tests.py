import unittest
from main import Solution

obj = Solution()


class MatrixTests(unittest.TestCase):

    def test_1(self):
        """[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] returns [1,2,3,6,9,8,7,4,5]"""
        self.assertEqual(obj.spiralOrder(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_2(self):
        """[[1,2,3,4],[5,6,7,8],[9,10,11,12]] returns [1,2,3,4,8,12,11,10,9,5,6,7]"""
        self.assertEqual(obj.spiralOrder(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

    def test_3(self):
        """[[7],[9],[6]] returns [7,9,6]"""
        self.assertEqual(obj.spiralOrder(
            [[7], [9], [6]]), [7, 9, 6])


if __name__ == '__main__':
    unittest.main()
