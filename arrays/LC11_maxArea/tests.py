import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) returns 49"""
        self.assertEqual(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_2(self):
        """maxArea([2, 3, 4, 5, 18, 17, 6]) returns 17"""
        self.assertEqual(obj.maxArea([2, 3, 4, 5, 18, 17, 6]), 17)


if __name__ == '__main__':
    unittest.main()
