import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """Works"""
        self.assertEqual(obj.search([1], 1), 0)
        self.assertEqual(obj.search([1, 3], 3), 1)
        self.assertEqual(obj.search([3, 1], 3), 0)
        self.assertEqual(obj.search([4, 5, 1, 2, 3], 1), 2)
        self.assertEqual(obj.search([7, 8, 1, 2, 3, 4, 5, 6], 2), 3)
        self.assertEqual(obj.search([4, 5, 6, 7, 0, 1, 2], 0), 4)


if __name__ == '__main__':
    unittest.main()
