import unittest
import LCA
from Node import Node

class testLCA(unittest.TestCase):

    def testContains(self):

        # Create tree
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        root.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEquals(LCA.contains(root, Node(3)), True, "Check if tree with root provided contains a specified node")
        self.assertEquals(LCA.contains(root, Node(9)), False, "Check contains() with node not in tree")

    def testgetLCA(self):

        # Create tree
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.right = Node(4)
        root.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEquals(LCA.getLCA(root, Node(3), Node(4)).id, 2, "Check LCA of two nodes contained in tree")
        self.assertEquals(LCA.getLCA(root, Node(0), Node(4)), None, "Check getLCA() when one node is not on tree")
        self.assertEquals(LCA.getLCA(root, Node(7), Node(2)).id, 1, "Check getLCA() with nodes of different depths")


if __name__ == '__main__':
    unittest.main()