import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """threeSum([2, 0, 1, -1]) returns [[-1, 0, 1]]"""
        res = obj.threeSum([2, 0, 1, -1])
        res[0].sort()
        self.assertEqual(res, [[-1, 0, 1]])

    def test_2(self):
        """threeSum([-1, 0, 1, 2, -1, -4]) returns [[-1, -1, 2], [-1, 0, 1]]"""
        res = obj.threeSum([-1, 0, 1, 2, -1, -4])
        for l in res:
            l.sort()
        self.assertEqual(res, [[-1, -1, 2], [-1, 0, 1]])

    def test_3(self):
        """No duplicate results returned"""
        res = obj.threeSum([-2, 0, 1, 1, 2])
        for l in res:
            l.sort()
        self.assertEqual(res, [[-2, 0, 2], [-2, 1, 1]])

        res = obj.threeSum([-2, 0, 0, 2, 2])
        res[0].sort()
        self.assertEqual(res, [[-2, 0, 2]])


if __name__ == '__main__':
    unittest.main()
