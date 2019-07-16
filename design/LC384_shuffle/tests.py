import unittest
from main import Solution


class DesignTests(unittest.TestCase):

    def test_1(self):
        """Shuffle works"""
        obj = Solution([num for num in range(0, 100)])
        final = None
        for i in range(0, 100):
            final = obj.shuffle()
        self.assertTrue(1 != final[1])

    def test_2(self):
        """Reset works"""
        array_100_nums = [num for num in range(0, 100)]
        obj = Solution(list(array_100_nums))
        obj.shuffle()
        self.assertEqual(obj.reset(), array_100_nums)
        obj.shuffle()
        self.assertEqual(obj.reset(), array_100_nums)


if __name__ == '__main__':
    unittest.main()
