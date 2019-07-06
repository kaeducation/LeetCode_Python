import unittest
from main import Solution

obj = Solution()


class DPTests(unittest.TestCase):

    def test_1(self):
        """uniquePaths(1, 1) --> 1"""
        self.assertEqual(obj.uniquePaths(1, 1), 1)

    def test_2(self):
        """uniquePaths(7, 3) --> 28"""
        self.assertEqual(obj.uniquePaths(7, 3), 28)

    def test_3(self):
        """uniquePaths(6, 3) --> 21"""
        self.assertEqual(obj.uniquePaths(6, 3), 21)


if __name__ == '__main__':
    unittest.main()
