import unittest
from main import Solution

obj = Solution()


class GraphTests(unittest.TestCase):

    def test_1(self):
        """works"""
        self.assertEqual(obj.countComponents(5, [[0, 1], [2, 1], [3, 4]]), 2)
        self.assertEqual(obj.countComponents(
            5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)


if __name__ == '__main__':
    unittest.main()
