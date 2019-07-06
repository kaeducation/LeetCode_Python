import unittest
from main import Solution

obj = Solution()


class StringTests(unittest.TestCase):

    def test_1(self):
        """'(', ')', '{', '}', '[', ']' should return False"""
        self.assertEqual(obj.isValid('('), False)
        self.assertEqual(obj.isValid(')'), False)
        self.assertEqual(obj.isValid('{'), False)
        self.assertEqual(obj.isValid('}'), False)
        self.assertEqual(obj.isValid('['), False)
        self.assertEqual(obj.isValid(']'), False)

    def test_2(self):
        """'(]', '([)]' should return False"""
        self.assertEqual(obj.isValid('(]'), False)
        self.assertEqual(obj.isValid('([)]'), False)

    def test_3(self):
        """'()', '()[]{}', '{[]}' should return True"""
        self.assertEqual(obj.isValid('()'), True)
        self.assertEqual(obj.isValid('()[]{}'), True)
        self.assertEqual(obj.isValid('{[]}'), True)


if __name__ == '__main__':
    unittest.main()
