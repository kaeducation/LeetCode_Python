import unittest
from main import Solution

obj = Solution()


class StringTests(unittest.TestCase):

    def test_1(self):
        """'abcabcbb' returns 3"""
        self.assertEqual(obj.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_2(self):
        """'pwwkew' returns 3"""
        self.assertEqual(obj.lengthOfLongestSubstring("pwwkew"), 3)

    def test_3(self):
        """'dvdf' returns 3"""
        self.assertEqual(obj.lengthOfLongestSubstring("dvdf"), 3)

    def test_4(self):
        """'bbb' returns 1"""
        self.assertEqual(obj.lengthOfLongestSubstring("bbb"), 1)


if __name__ == '__main__':
    unittest.main()
