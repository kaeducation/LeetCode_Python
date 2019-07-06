import unittest
from main import Solution

obj = Solution()


class IntervalTests(unittest.TestCase):

    def test_1(self):
        """merge([[1, 4], [2, 3]]) --> [1, 4]"""
        self.assertEqual(obj.merge([[1, 4], [2, 3]]), [[1, 4]])

    def test_2(self):
        """merge([[1, 4], [4, 5]]) --> [1, 5]"""
        self.assertEqual(obj.merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_3(self):
        """merge([[1,3],[2,6],[8,10],[15,18]]) --> [[1,6],[8,10],[15,18]]"""
        self.assertEqual(obj.merge(
            [[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])


if __name__ == '__main__':
    unittest.main()
