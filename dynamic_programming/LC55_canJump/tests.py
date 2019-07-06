import unittest
from main import Solution

obj = Solution()


class DPTests(unittest.TestCase):

    def test_1(self):
        """[2, 3, 1, 1, 4] returns True"""
        self.assertEqual(obj.canJump([2, 3, 1, 1, 4]), True)

    def test_2(self):
        """[3] returns True"""
        self.assertEqual(obj.canJump([3]), True)

    def test_3(self):
        """[3,2,1,0,4] returns False"""
        self.assertEqual(obj.canJump([3, 2, 1, 0, 4]), False)


if __name__ == '__main__':
    unittest.main()
