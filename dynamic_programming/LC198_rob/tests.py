import unittest
from main import Solution

obj = Solution()


class DPTests(unittest.TestCase):

    def test_1(self):
        """rob([1,2,3,1]) returns 4"""
        self.assertEqual(obj.rob([1, 2, 3, 1]), 4)

    def test_2(self):
        """rob([2,1,1,2]) returns 4"""
        self.assertEqual(obj.rob([2, 1, 1, 2]), 4)

    def test_3(self):
        """rob([]) returns 0"""
        self.assertEqual(obj.rob([]), 0)


if __name__ == '__main__':
    unittest.main()
