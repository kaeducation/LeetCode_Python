import unittest
from main import Solution

obj = Solution()


class DPTests(unittest.TestCase):

    def test_1(self):
        """lengthOfLIS([10,9,2,5,3,7,101,4]) returns 4 since LIS is [2,3,7,101]"""
        self.assertEqual(obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 4]), 4)

    def test_2(self):
        """lengthOfLIS([0]) returns 1"""
        self.assertEqual(obj.lengthOfLIS([0]), 1)

    def test_3(self):
        """lengthOfLIS([-2, -1]) returns 2"""
        self.assertEqual(obj.lengthOfLIS([-2, -1]), 2)

    def test_4(self):
        """lengthOfLIS([]) returns 0"""
        self.assertEqual(obj.lengthOfLIS([]), 0)


if __name__ == '__main__':
    unittest.main()
