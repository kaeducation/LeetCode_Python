import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """Works"""
        self.assertEqual(obj.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(obj.longestConsecutive([100, 4, 200, 1, 2]), 2)
        self.assertEqual(obj.longestConsecutive([0, -1]), 2)


if __name__ == '__main__':
    unittest.main()
