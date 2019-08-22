import unittest
from main import Solution, Node

obj = Solution()


class GraphTests(unittest.TestCase):

    def test_1(self):
        """Works for valid graph"""
        one_node = Node(1, [])
        two_node = Node(2, [])

        one_node.neighbors = [two_node]
        two_node.neighbors = [one_node]

        res_node = obj.cloneGraph(one_node)
        self.assertEqual(res_node != one_node, True)

        self.assertEqual(len(res_node.neighbors), 1)
        two_node_clone = res_node.neighbors[0]
        self.assertEqual(two_node_clone != two_node, True)
        self.assertEqual(len(two_node_clone.neighbors), 1)
        self.assertEqual(two_node_clone.neighbors[0] == res_node, True)


if __name__ == '__main__':
    unittest.main()
