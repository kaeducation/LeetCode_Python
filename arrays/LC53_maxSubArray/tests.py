import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) returns 6 for [4,-1,2,1]"""
        self.assertEqual(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


if __name__ == '__main__':
    unittest.main()
