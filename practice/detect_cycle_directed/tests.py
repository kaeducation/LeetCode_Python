import unittest
from main import Solution

obj = Solution()


class PracticeTests(unittest.TestCase):

    def test_2(self):
        """returns False correctly"""
        self.assertEqual(obj.hasCycle(
            2, [[0, 1]]), False)

        self.assertEqual(obj.hasCycle(
            4, [[0, 1], [0, 2], [1, 2]]), False)
        #  0
        #  |  \
        #  v    >
        #  1 ->  2

    def test_1(self):
        """returns True correctly"""
        self.assertEqual(obj.hasCycle(
            1, [[0, 0]]), True)

        self.assertEqual(obj.hasCycle(
            3, [[0, 1], [2, 1], [2, 2]]), True)

        self.assertEqual(obj.hasCycle(
            4, [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]), True)


if __name__ == '__main__':
    unittest.main()
