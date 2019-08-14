import unittest
from main import Solution

obj = Solution()


class PracticeTests(unittest.TestCase):

    def test_1(self):
        """returns False correctly"""
        self.assertEqual(obj.hasCycle(2, [[0, 1]]), False)
        self.assertEqual(obj.hasCycle(3, [[1, 0], [1, 2]]), False)

    def test_2(self):
        """returns True correctly"""
        self.assertEqual(obj.hasCycle(
            4, [[1, 0], [0, 3], [1, 2], [2, 3]]), True)

        self.assertEqual(obj.hasCycle(
            5, [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]), True)


if __name__ == '__main__':
    unittest.main()
