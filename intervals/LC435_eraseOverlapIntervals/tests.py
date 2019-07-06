import unittest
from main import Solution

obj = Solution()


class IntervalTests(unittest.TestCase):

    def test_1(self):
        """eraseOverlapIntervals([]) and eraseOverlapIntervals([[1,2]]) return 0"""
        self.assertEqual(obj.eraseOverlapIntervals([]), 0)
        self.assertEqual(obj.eraseOverlapIntervals([[1, 2]]), 0)

    def test_2(self):
        """eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]] ) returns 2"""
        self.assertEqual(obj.eraseOverlapIntervals(
            [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]), 2)

    def test_3(self):
        """eraseOverlapIntervals([[1, 100], [1, 2], [3, 4], [2, 3]] ) returns 1"""
        self.assertEqual(obj.eraseOverlapIntervals(
            [[1, 100], [1, 2], [3, 4], [2, 3]]), 1)


if __name__ == '__main__':
    unittest.main()
