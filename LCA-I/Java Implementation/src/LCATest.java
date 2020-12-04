import static org.junit.Assert.*;

import org.junit.Test;

public class LCATest {
	
	public Node root;
	
	//For simplisity sake for this particular program
	public void createTree() {
		root = new Node(1);
		root.left = new Node(2);
		root.left.left = new Node(3);
		root.left.right = new Node(4); 
		root.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7);
	} 

	@Test
	public void testContains() {
		
		createTree();		
		
		assertTrue("Check if contains() can navigate left and right to a leaf node", LCA.contains(root, new Node(4)));
		assertFalse("Check node not contained in supplied tree", LCA.contains(root, new Node(8))); 
	}
	
	//Tests both getLCA and getLCAr
	@Test
	public void testGetLCA() {

		createTree();
		
		assertEquals("Check LCA where one node is the root", 1, LCA.getLCA(root, new Node(1), new Node(1)).id);
		assertEquals("Check LCA of two nodes contained on tree where LCA is not the root", 2, LCA.getLCA(root, new Node(3), new Node(4)).id); 
		assertEquals("Check LCA of two nodes contained on tree at different depths", 1, LCA.getLCA(root, new Node(3), new Node(7)).id);
		assertNull("Check LCA of when first node isn't contained on the tree", LCA.getLCA(root, new Node(9), new Node(7))); 
		assertNull("Check LCA of when second node isn't contained on the tree", LCA.getLCA(root, new Node(1), new Node(9))); //For the sake of full code coverage
		
	}

}
