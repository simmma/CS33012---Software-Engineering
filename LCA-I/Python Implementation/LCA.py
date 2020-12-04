# Program that generates a
# binary tree and can evaluate
# the lowest common ancestor of two nodes
# (New language)

from Node import Node

# class Node:
#     def __init__(self, id):
#         self.id = id
#         self.left = None		# Null
#         self.right = None		# Null


# class LCA:
# Recursive funtion to evaluate LCA
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


def getLCA(root, node1, node2):
    if(contains(root, node1) and contains(root, node2)):
        return getLCAr(root, node1, node2)
    else:
        return None

# Evaluates if a node is a child of another supplied node(curr)


def contains(curr, node):
    if(curr == None):
        return False
    elif(curr.id == node.id):
        return True
    else:
        return (contains(curr.left, node) or contains(curr.right, node))


# def main():
#     # Create tree
#     root = Node(1)
#     root.left = Node(2)
#     root.left.left = Node(3)
#     root.left.right = Node(4)
#     root.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)

#     # Prompts for node ids
#     node1 = int(input("Enter id of first node:"))
#     node2 = int(input("Enter id of second node:"))

#     LCA = getLCA(root, Node(node1), Node(node2))

#     # Print results of LCA evaluation
#     if(LCA != None):
#         print("LCA of " + str(node1) + " and " +
#               str(node2) + " is " + str(LCA.id))
#     else:
#         print("No LCA found")


# main()
