class Node:
    def __init__(self, id):
        self.id = id            # Assume Unique id
        self.children = []
    
    def addChildNode(self, parentID, childID):
        parentNode = self.searchNode(parentID)
        if parentNode is not None:      # Parent node exists
            # TODO add test for non-cyclicalness
            parentNode.children.append(Node(childID))

    #Otherwise do nothing...


    # # Navigate to node with ID 
    # # Returns node if found, otherwise None
    def searchNode(self, nodeID):
        if(self.id == nodeID):
            return self
        elif not self.children: #pythonic way to check emptyness
            return None 
        else:
            for i in range(len(self.children)):
                result = self.children[i].searchNode(nodeID) # result???
                if result is not None:
                    return result
            #Otherwise
            return None
            