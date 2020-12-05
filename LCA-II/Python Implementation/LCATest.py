import unittest
import LCA
from Node import Node

class testLCA(unittest.TestCase):

    # Test to check tree building functionality
    def testAddChildNode(self):
        #Check leaf nodes
        root = Node(1)
        self.assertEqual(root.children, [], "Should not contain any nodes")

        #Create tree
        # 1 = [2, 3, 4, 5], 2 = [4], 3 = [4, 5], 4 = [5], 5 = []
        root.addChildNode(1, 2)
        root.addChildNode(1, 3)
        root.addChildNode(1, 4)
        root.addChildNode(1, 5)
        root.addChildNode(2, 4)
        root.addChildNode(3, 4)
        root.addChildNode(3, 5)
        root.addChildNode(4, 5)

        #check children of root
        listID = []
        for i in range(len(root.children)):
            listID.append(root.children[i].id)
        self.assertEqual(listID, [2, 3, 4, 5], "Check if all children can be found from the root node")
        
        #check children of non-root node
        listID.clear()
        currNode = root.searchNode(4)
        for i in range(len(currNode.children)):
           listID.append(currNode.children[i].id)
        self.assertEqual(listID, [5], "Check if non-root node can be found and accessed")

        # Try to add a node cyclically
        # self.assertEqual(addChildNode(root, 5, 1), -1, "Checks node can't be added cyclically")

    def testSearchNode(self):
        #Create tree
        # 1 = [2, 3, 4, 5], 2 = [4], 3 = [4, 5], 4 = [5], 5 = [6], 6 = []
        root = Node(1)
        root.addChildNode(1, 2)
        root.addChildNode(1, 3)
        root.addChildNode(1, 4)
        root.addChildNode(1, 5)
        root.addChildNode(2, 4)
        root.addChildNode(3, 4)
        root.addChildNode(3, 5)
        root.addChildNode(4, 5)
        root.addChildNode(5, 6)

        self.assertTrue(root.searchNode(3), "Check if tree with root provided contains a specified node")
        self.assertFalse(root.searchNode(9), "Check if tree with root provided contains a specified node not in tree")

        # search and addChildNode are dependent on one another, best way to test?
        self.assertTrue(root.searchNode(6), "Check if tree contains a specified node that's not a child of the root")
        
    def testgetLCA(self):
        #Create tree
        # 1 = [2, 3, 4, 5], 2 = [4], 3 = [4, 5], 4 = [5], 5 = [6], 6 = []
        root = Node(1)
        root.addChildNode(1, 2)
        root.addChildNode(1, 3)
        root.addChildNode(1, 4)
        root.addChildNode(1, 5)
        root.addChildNode(2, 4)
        root.addChildNode(3, 4)
        root.addChildNode(3, 5)
        root.addChildNode(4, 5)
        root.addChildNode(5, 6)

        self.assertIsNone(LCA.getLCA(root, []), "Check LCA of no nodes contained in tree")     # How to check if [] or None??
        self.assertEqual(LCA.getLCA(root, [4]), 4, "Check LCA of one nodes contained in tree")
        self.assertIsNone(LCA.getLCA(root, [9]),"Check LCA of one nodes not in tree")
        self.assertIsNone(LCA.getLCA(root, [2, 8]), "Check getLCA() when one node is not on tree")
        #self.assertEqual(LCA.getLCA(root, [4, 5]), 2, "Check LCA of two nodes contained in tree")
        #self.assertEqual(LCA.getLCA(root, [4, 5, 2]), 2, "Check LCA of three nodes contained in tree")
        
if __name__ == '__main__':
    unittest.main()