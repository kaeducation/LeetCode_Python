import unittest
from main import Solution

obj = Solution()


class ArrayTests(unittest.TestCase):

    def test_1(self):
        """twoSum([2,7,11,15], 9) returns [0,1]"""
        self.assertEqual(sorted(obj.twoSum([2, 7, 11, 15], 9)), [0, 1])

    def test_2(self):
        """twoSum([3, 2, 4], 6) returns [1,2]"""
        self.assertEqual(sorted(obj.twoSum([3, 2, 4], 6)), [1, 2])


if __name__ == '__main__':
    unittest.main()
