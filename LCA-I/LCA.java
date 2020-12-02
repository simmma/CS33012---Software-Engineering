import java.util.*;
public class LCA {
	
	/* This program creates a binary tree and can 
	* perform a lowest common ancestor evaluation 
	*on two node of this tree
	*/


	public static void main(String args[]) {
		//Create binary tree
		Node root = new Node(1);
		root.left = new Node(2);
		root.left.left = new Node(3);
		root.left.right = new Node(4);
		root.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7);

		//System.out.println(root.id);
		Scanner scan = new Scanner(System.in);

		int a = scan.nextInt();
		int b = scan.nextInt();

		Node LCANode = getLCA(root, new Node(a), new Node(b));

		System.out.println("LCA of " + a + " and " + b + " is " + LCANode.id);
	}

	public static Node getLCA(Node root, Node node1, Node node2) {
		if(root == null) {
			return null;
		}
		//System.out.println(root.id);
		if(root.id == node1.id || root.id == node2.id) {
			return root;
		}
		Node lef = getLCA(root.left, node1, node2);
		Node rig = getLCA(root.right, node1, node2);

		if(lef != null && rig != null) {
			return root;
		} else if (lef == null && rig == null) {
			return null;
		} else {
			return (lef == null)?rig:lef;
		}
	}
}

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
