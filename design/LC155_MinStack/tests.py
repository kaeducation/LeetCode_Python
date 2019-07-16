import unittest
from main import MinStack


class DesignTests(unittest.TestCase):

    def test_1(self):
        """top() works for empty and filled out stack"""
        min_stack = MinStack()
        min_stack.top()
        min_stack.push(11)
        self.assertEqual(min_stack.top(), 11)
        min_stack.push(13)
        self.assertEqual(min_stack.top(), 13)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 11)

    def test_2(self):
        """getMin() works for empty and filled out stack"""
        min_stack = MinStack()
        min_stack.getMin()
        min_stack.push(-2)
        self.assertEqual(min_stack.getMin(), -2)
        min_stack.push(0)
        self.assertEqual(min_stack.getMin(), -2)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), -2)


if __name__ == '__main__':
    unittest.main()
