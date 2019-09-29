import unittest
from main import Trie


class TreeTests(unittest.TestCase):

    def test_1(self):
        """insert() and search() work."""
        trie = Trie()
        trie.insert('apple')

        self.assertEqual(trie.search('apple'), True)
        self.assertEqual(trie.search('app'), False)

        trie.insert('app')

        self.assertEqual(trie.search('app'), True)

    def test_2(self):
        """startsWith() works properly"""
        trie = Trie()
        trie.insert('apple')

        self.assertEqual(trie.startsWith('app'), True)
        self.assertEqual(trie.startsWith('apl'), False)


if __name__ == '__main__':
    unittest.main()
