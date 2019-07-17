import unittest
from main import Solution


class DesignTests(unittest.TestCase):

    def test_1(self):
        """Shuffle works"""
        deck_of_cards = Solution([num for num in range(52)])
        deck_of_cards2 = Solution([num for num in range(52)])
        result_shuffle = deck_of_cards.shuffle()
        result_shuffle2 = deck_of_cards2.shuffle()
        self.assertEqual(result_shuffle == result_shuffle2, False)

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
