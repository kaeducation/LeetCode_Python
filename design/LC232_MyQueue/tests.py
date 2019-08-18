import unittest
from main import MyQueue


class DesignTests(unittest.TestCase):

    def test_1(self):
        """Push and pop work"""
        queue = MyQueue()

        queue.push(1)
        queue.push(2)
        queue.push(3)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.pop(), 3)

    def test_2(self):
        """Peek and empty work"""
        queue = MyQueue()

        queue.push(1)
        self.assertEqual(queue.peek(), 1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
        queue.push(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.empty(), False)

        queue.pop()
        self.assertEqual(queue.peek(), 2)
        queue.pop()
        self.assertEqual(queue.peek(), 3)
        queue.pop()
        self.assertEqual(queue.empty(), True)


if __name__ == '__main__':
    unittest.main()
