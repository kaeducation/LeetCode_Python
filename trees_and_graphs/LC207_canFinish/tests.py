import unittest
from main import Solution

obj = Solution()


class GraphTests(unittest.TestCase):

    def test_1(self):
        """returns False correctly"""
        self.assertEqual(obj.canFinish(
            1, [[0, 0]]), False)

        self.assertEqual(obj.canFinish(
            3, [[0, 1], [2, 1], [2, 2]]), False)

        self.assertEqual(obj.canFinish(
            4, [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]), False)

    def test_2(self):
        """returns True correctly"""
        self.assertEqual(obj.canFinish(
            2, [[0, 1]]), True)

        self.assertEqual(obj.canFinish(
            4, [[0, 1], [0, 2], [1, 2]]), True)
        #  0
        #  |  \
        #  v    >
        #  1 ->  2


if __name__ == '__main__':
    unittest.main()
