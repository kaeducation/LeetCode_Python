import unittest
from main import WordDictionary


class TreeTests(unittest.TestCase):

    def test_1(self):
        """addWord and search works"""
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")

        self.assertEqual(wd.search('pad'), False)
        self.assertEqual(wd.search('ba'), False)

        self.assertEqual(wd.search('bad'), True)
        self.assertEqual(wd.search('.ad'), True)
        self.assertEqual(wd.search('b..'), True)


if __name__ == '__main__':
    unittest.main()
