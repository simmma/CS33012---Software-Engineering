import unittest
import LCA
from Node import Node

class testLCA(unittest.TestCase):

    # Test to check tree building functionality
    def testNode(self):

        #self.assertEqual(Node(0).children, [], "Should not contain any nodes")

        #Create tree
        # 1 = [2, 3, 4, 5], 2 = [4], 3 = [4, 5], 4 = [5], 5 = []
        root = Node(1)
        # addChildNode(root, parentNodeID, childNodeID)
        # addChildNode(root, 1, 2)
        # addChildNode(root, 2, 4)

        #check children
        listID = []
        #for i in range(len(root.children)):
        #    listID.append(root.children[i])
        #self.assertEqual(listID, [2, 3, 4, 5], "Check if all children can be found from the root node")
        
        #currNode = searchNode(root, nodeID)
        listID.clear()
        #for i in range(len(currNode.children)):
        #    listID.append(currNode.id)
        #self.assertEqual(listID, [4], "Check if non-root node can be found and accessed")

        # Try to add a node cyclically
        # self.assertEqual(addChildNode(root, 5, 1), -1, "Checks node can't be added cyclically")

    def testSearchNode(self):

        # Check None arguments

        #Create tree
        # 1 = [2, 3, 4, 5], 2 = [4], 3 = [4, 5], 4 = [5], 5 = []
        root = Node(1)
        # addChildNode(root, parentNodeID, childNodeID)
        # addChildNode(root, 1, 2)
        # addChildNode(root, 2, 4)

        #self.assertTrue(Node.searchNode(root, Node(3)), "Check if tree with root provided contains a specified node")
        #self.assertFalse(Node.searchNode(root, Node(9)), "Check contains() with node not in tree")

    def testgetLCA(self):

        # Check None arguments

        #Create tree
        # 1 = [2, 3, 4, 5], 2 = [4], 3 = [4, 5], 4 = [5], 5 = []
        root = Node(1)
        # addChildNode(root, parentNodeID, childNodeID)
        # addChildNode(root, 1, 2)
        # addChildNode(root, 2, 4)

        #self.assertEqual(LCA.getLCA(root, [4, 5]).id, 2, "Check LCA of two nodes contained in tree")
        #self.assertEqual(LCA.getLCA(root, [4, 5, 2]).id, 2, "Check LCA of three nodes contained in tree")
        #self.assertIsNone(LCA.getLCA(root, [2, 8]), "Check getLCA() when one node is not on tree")
        


if __name__ == '__main__':
    unittest.main()