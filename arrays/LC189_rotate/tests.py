import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """Works"""
        original = [1, 2, 3, 4, 5, 6, 7]
        obj.rotate(original, 1)
        self.assertEqual(original, [7, 1, 2, 3, 4, 5, 6])

        original.sort()
        obj.rotate(original, 30)
        self.assertEqual(original, [6, 7, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
