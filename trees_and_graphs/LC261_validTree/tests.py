import unittest
from main import Solution

obj = Solution()


class GraphTests(unittest.TestCase):

    def test_1(self):
        """Returns True correctly"""
        self.assertEqual(obj.validTree(
            5,  [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
        self.assertEqual(obj.validTree(
            5, [[1, 0], [0, 2], [0, 3], [3, 4]]), True)

    def test_2(self):
        """Returns False due to seperate components"""
        self.assertEqual(obj.validTree(4, [[0, 1], [2, 3]]), False)

    def test_3(self):
        """Returns False due to cycle"""
        self.assertEqual(obj.validTree(
            5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)


if __name__ == '__main__':
    unittest.main()
