import unittest
from main import Solution

obj = Solution()


class StringTests(unittest.TestCase):

    def test_1(self):
        """isAnagram('anagram', 'nagaram') returns True"""
        self.assertEqual(obj.isAnagram('anagram', 'nagaram'), True)

    def test_2(self):
        """isAnagram('rat', 'car') returns False"""
        self.assertEqual(obj.isAnagram('rat', 'car'), False)

    def test_3(self):
        """isAnagram('', '') returns True"""
        self.assertEqual(obj.isAnagram('', ''), True)

    def test_4(self):
        """isAnagram('aacc', 'ccac') returns False"""
        self.assertEqual(obj.isAnagram('aacc', 'ccac'), False)

    def test_5(self):
        """isAnagram('ab', 'a') returns False"""
        self.assertEqual(obj.isAnagram('ab', 'a'), False)


if __name__ == '__main__':
    unittest.main()
