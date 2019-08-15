import unittest
from main import Solution

obj = Solution()


class PracticeTests(unittest.TestCase):

    def test_1(self):
        """works"""
        input1 = [2, 0, 2, 1, 1, 0]
        obj.sortColors(input1)
        self.assertEqual(input1, [0, 0, 1, 1, 2, 2])

        input2 = [2]
        obj.sortColors(input2)
        self.assertEqual(input2, [2])


if __name__ == '__main__':
    unittest.main()
