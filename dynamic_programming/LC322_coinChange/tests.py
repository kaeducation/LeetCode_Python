import unittest
from main import Solution

obj = Solution()


class DPTests(unittest.TestCase):

    def test_1(self):
        """[1, 2, 5], 11 should return 3 for 5 + 5 + 1"""
        self.assertEqual(obj.coinChange([1, 2, 5], 11), 3)

    def test_2(self):
        """[2, 5, 10, 1], 27 should return 4 for 10 + 10 + 5 + 2"""
        self.assertEqual(obj.coinChange([2, 5, 10, 1], 27), 4)

    def test_3(self):
        """[2], 3 should return -1 since change is not possible"""
        self.assertEqual(obj.coinChange([2], 3), -1)


if __name__ == '__main__':
    unittest.main()
