package DataStructures;

import java.lang.Comparable;


public class AVLTree {
	
	private AVLNode root; 
	private int size; 
	
	public AVLTree() {
		this.root = null;
		this.size = 0;
	}
	
	public AVLNode find(Comparable key) {
		return find(this.root, key);
	}
	
	private AVLNode find(AVLNode node, Comparable key) {
		if(node == null) {
			return null; 
		} else if(key.compareTo(node.key()) < 0) {
			return find(node.left(), key);
		} else if(key.compareTo(node.key()) > 0) {
			return find(node.right(), key);
		} else return node; 
	}
	
	public void insert(Comparable key) {
		root = insert(this.root, key);
	}
	
	public <T> void delete(Comparable<T> key) {
		root = delete(this.root, key);
	}
	
	private AVLNode insert(AVLNode node, Comparable key) {
		AVLNode newRoot;
		/*A*/
		if(node == null) {
			newRoot = new AVLNode(key);
			this.size++;
		}
		/*B*/
		//search left subtree
		else if(key.compareTo(node.key()) < 0) {
			newRoot = insert(node.left(), key);
			node.setLeft(newRoot);
			newRoot.setParent(node);
			
			//rebalance
			if(node.balanceFactor() == 2) {
				if(node.left().balanceFactor() > 0) {
					newRoot = singleRightRotate(node);
				} else {
					newRoot = doubleRightRotate(node);
				}
			} else {
				newRoot = node;
			}
		} 
		/*C*/
		//search right subtree
		else if(key.compareTo(node.key()) > 0) {
			newRoot = insert(node.right(), key);
			node.setRight(newRoot);
			newRoot.setParent(node);
			
			//rebalance
			if(node.balanceFactor() == -2) {
				if(node.right().balanceFactor() < 0) {
					newRoot = singleLeftRotate(node);
				} else {
					newRoot = doubleLeftRotate(node); 
				}
			} else {
				newRoot = node; 
			}
		}
		//key already in tree; increase frequency 
		else {
			node.incFreq();
			newRoot = node; 
		}
		
		/* Adjust Height */
		newRoot.setHeight();
		
		return newRoot; 
	}

	private AVLNode delete(AVLNode node, Comparable key) {
		AVLNode newRoot;
		/*A*/
		if(node == null) {
			System.out.println("Key not in tree");
			return node; 
		}
		/*B*/
		//search left subtree
		else if(key.compareTo(node.key()) < 0) {
			newRoot = delete(node.left(), key);
			node.setLeft(newRoot);
			if(newRoot != null) newRoot.setParent(node);
			
			//rebalance
			if(node.balanceFactor() == -2) {
				if(node.right().balanceFactor() < 0) {
					newRoot = singleLeftRotate(node);
				} else {
					newRoot = doubleLeftRotate(node);
				}
			} else {
				newRoot = node;
			}
		} 
		/*C*/
		//search right subtree
		else if(key.compareTo(node.key()) > 0) {
			newRoot = delete(node.right(), key);
			node.setRight(newRoot);
			if(newRoot != null) newRoot.setParent(node);
			
			//rebalance
			if(node.balanceFactor() == 2) {
				if(node.left().balanceFactor() > 0) {
					newRoot = singleRightRotate(node);
				} else {
					newRoot = doubleRightRotate(node); 
				}
			} else {
				newRoot = node; 
			}
		}
		//key already in tree; decrease frequency or delete 
		else {
			if(node.frequency() > 1) {
				node.decFreq();
				newRoot = node; 
			} else {
				this.size--;
				//leaf
				if((node.left() == null) && (node.right() == null)) {
					return null; //WAS newRoot = null, but want to bypass setHeight();
				}
				//1 child
				else if((node.left() == null) ^ (node.left() == null)) {
					newRoot = (node.left() != null) ? node.left() : node.right();
				}
				//2 children 
				else {
					AVLNode max = max(node.left()); //finding maximum of left subtree
					max.setFreq(1);
					Comparable newKey = max.key();
					int newFreq = max.frequency();
					newRoot = delete(node, max.key());
					node.setKey(newKey);
					node.setFreq(newFreq);
				}
			}
		}
		
		/* Adjust Height */
		newRoot.setHeight();
		
		return newRoot; 
	}
	
	private AVLNode singleLeftRotate(AVLNode A) {
		AVLNode B = A.right();
		A.setRight(B.left());
		if(A.right() != null) A.right().setParent(A); 
		B.setLeft(A);
		A.setParent(B);
		
		A.setHeight();
		B.setHeight(); //technically don't need
		return B; 
	}
	
	private AVLNode doubleLeftRotate(AVLNode A) {
		AVLNode B = A.right();
		AVLNode C = B.left();
		
		B.setLeft(C.right());
		if(B.left() != null) B.left().setParent(B);
		
		A.setRight(C.left());
		if(A.right() != null) A.right().setParent(A);
		
		C.setLeft(A);
		A.setParent(C);
		
		C.setRight(B);
		B.setParent(C);
		
		A.setHeight();
		B.setHeight();
		C.setHeight(); //technically don't need
		return C;
	}
	
	private AVLNode singleRightRotate(AVLNode A) {
		AVLNode B = A.left();
		A.setLeft(B.right());
		if(A.left() != null) A.left().setParent(A);
		B.setRight(A);
		A.setParent(B);
		
		A.setHeight();
		B.setHeight(); //technically don't need
		return B; 
	}
	
	private AVLNode doubleRightRotate(AVLNode A) {
		AVLNode B = A.left();
		AVLNode C = B.right();
		
		B.setRight(C.left());
		if(B.right() != null) B.right().setParent(B);
		
		A.setLeft(C.right());
		if(A.left() != null) A.left().setParent(A);
		
		C.setRight(A);
		A.setParent(C);
		
		C.setLeft(B);
		B.setParent(C);
		
		A.setHeight();
		B.setHeight();
		C.setHeight(); //technically don't need
		return C;
	}

	private AVLNode max(AVLNode node) {
		if(node.right() == null) return node;
		else return max(node.right());
	}
	
	public int size() {
		return this.size;
	}
	
	public void printTree() {
		printTree(this.root);
		System.out.println();
	}
	
	private void printTree(AVLNode node) {
		System.out.print("(");
		if(node != null) {
			System.out.print(node.key() + ", " + node.height(node) + " ");
			printTree(node.left());
			printTree(node.right());
		}
		System.out.print(")");
	}

	
	public static void main(String args[]) {
		AVLTree tree = new AVLTree();
		tree.insert(10);
		tree.insert(5);
		tree.insert(30);
		tree.insert(6);
		tree.insert(20);
		tree.insert(35);
		tree.insert(25);
		tree.insert(25);
		tree.printTree();
		tree.delete(25);
		tree.delete(25);
		tree.printTree();
	}
}
