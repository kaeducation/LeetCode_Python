import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """maxProfit([7, 1, 5, 3, 6, 4]) --> 5"""
        self.assertEqual(obj.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_2(self):
        """maxProfit([7, 6, 4, 3, 1]) --> 0"""
        self.assertEqual(obj.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == '__main__':
    unittest.main()
