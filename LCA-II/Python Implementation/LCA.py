# Program that generates a
# binary tree and can evaluate
# the lowest common ancestor of two nodes
# (New language)

from Node import Node

#Recursive funtion to evaluate LCA
def getLCAr(curr, node1, node2):
    if(curr == None):
        return None
    if(curr.id == node1.id or curr.id == node2.id):
        return curr
    else:
        lef = getLCAr(curr.left, node1, node2)
        rig = getLCAr(curr.right, node1, node2)

        if(lef != None and rig != None):
            return curr
        elif(lef == None and rig == None):
            return None
        else:
            return rig if (lef == None) else lef

# Set-up for recursive function to find LCA of two nodes in a tree reference by it's root node
# Returns id of Node that is LCA
def getLCA(root, nodeList):
    if len(nodeList) >= 2:
        node1 = root.searchNode(nodeList[0])
        if node1 is None:   # Node is not in tree
            return None
        for i in range(1, len(nodeList)):
            node2 = root.searchNode(nodeList[i])
            if node2 is None:
                return None
            else:
                node1 = getLCAr(root, node1, node2)  
        return node1    #Contains LCA   
    elif len(nodeList) == 1:
        node1 = root.searchNode(nodeList[0])
        if node1 is None:
            return None
        else:
            return nodeList[0]
    elif len(nodeList) == 0:
        return None