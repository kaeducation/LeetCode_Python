import unittest
from main import Solution

obj = Solution()


class StringTests(unittest.TestCase):

    def test_1(self):
        """'cbbd' returns 'bb'"""
        self.assertEqual(obj.longestPalindrome('cbbd'), 'bb')

    def test_2(self):
        """'abba' returns 'abba'"""
        self.assertEqual(obj.longestPalindrome("abba"), "abba")

    def test_3(self):
        """'abacdfgdcaba' returns 'aba'"""
        self.assertEqual(obj.longestPalindrome("abacdfgdcaba"), "aba")

    def test_4(self):
        """'a' returns 'a'"""
        self.assertEqual(obj.longestPalindrome("a"), "a")


if __name__ == '__main__':
    unittest.main()
