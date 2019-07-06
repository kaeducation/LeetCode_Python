import unittest
from main import Solution

obj = Solution()


class DPTests(unittest.TestCase):

    def test_1(self):
        """Returns 1 way to climb 1 stair"""
        self.assertEqual(obj.climbStairs(1), 1)

    def test_2(self):
        """Returns 2 ways to climb 2 stairs"""
        self.assertEqual(obj.climbStairs(2), 2)

    def test_3(self):
        """Returns 3 ways to climb 3 stairs"""
        self.assertEqual(obj.climbStairs(3), 3)

    def test_4(self):
        """Returns 5 ways to climb 4 stairs"""
        self.assertEqual(obj.climbStairs(4), 5)


if __name__ == '__main__':
    unittest.main()
