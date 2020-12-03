import java.util.*;
public class LCA {
	
	/* This program creates a predefined binary tree and can 
	* perform a lowest common ancestor evaluation 
	* on two nodes of this tree
	*/

	//(Old language)

	public static void main(String args[]) {
		//Create binary tree
		Node root = new Node(1);
		root.left = new Node(2);
		root.left.left = new Node(3);
		root.left.right = new Node(4);
		root.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7);

		//Prompts for node ids
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter id of first node: ");
		int a = scan.nextInt();
		System.out.print("Enter id of second node: ");
		int b = scan.nextInt();

		//Evaluate LCA
		Node LCANode = getLCA(root, new Node(a), new Node(b));

		//Print results of LCA evaluation
		if(LCANode != null) {
			System.out.println("LCA of " + a + " and " + b + " is " + LCANode.id);
		} else {
			System.out.println("No LCA found");
		}

	}

	// set up for recursive getLCAr() calls
	public static Node getLCA(Node root, Node node1, Node node2) {
		if(contains(root, node1) && contains(root, node2)) {
			return getLCAr(root, node1, node2);
		}
		return null;
	}

	// Recursively evaluate the lowest common ancestor
	public static Node getLCAr(Node root, Node node1, Node node2) {
		if(root == null) {
			return null;
		}
		if(root.id == node1.id || root.id == node2.id) {
			return root;
		}

		Node lef = getLCAr(root.left, node1, node2);
		Node rig = getLCAr(root.right, node1, node2);

		if(lef != null && rig != null) {
			return root;
		} else if (lef == null && rig == null) {
			return null;
		} else {
			return (lef == null)?rig:lef;
		}
	}

	// Recursively evaluates if a node is a child of another supplied node(curr)
	public static Boolean contains(Node curr, Node node) {
		if(curr == null) {
			return false;
		} else if (curr.id == node.id) {
			return true;
		} else {
			return (contains(curr.left, node) || contains(curr.right, node));
		}
	}
}

// Definition of type Node
class Node {
	Node left;
	Node right;
	int id;

	public Node(int id) {
		this.left = null;
		this.right = null;
		this.id = id;
	}
}
