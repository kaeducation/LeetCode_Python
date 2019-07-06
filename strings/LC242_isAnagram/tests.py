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


if __name__ == '__main__':
    unittest.main()
