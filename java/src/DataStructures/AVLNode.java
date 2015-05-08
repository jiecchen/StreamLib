package DataStructures;

import java.lang.Comparable;

public class AVLNode { 
	
	private AVLNode parent;
	private AVLNode left;
	private AVLNode right;
	private Comparable key;
	private int frequency;
	private int height;
	
	public AVLNode() {
		this.parent = null;
		this.left = null;
		this.right = null;
		this.height = -1; 
	}
	
	public AVLNode(Comparable key) {
		this();
		this.key = key;
		this.frequency = 1;
		this.height = 0;
	}
	
	public static int height(AVLNode node) {
		if(node == null) {
			return -1;
		} else return node.height;
	}
	
	public Comparable key() {
		return this.key;
	}
	
	protected <T> void setKey(Comparable<T> key) {
		this.key = key;
	}
	
	public int frequency() {
		return this.frequency;
	}
	
	protected void incFreq() {
		this.frequency++;
	}
	
	protected void decFreq() {
		this.frequency--;
	}
	
	protected void setFreq(int freq) {
		this.frequency = freq; 
	}
	
	public AVLNode left() {
		return this.left;
	}
	
	public AVLNode right() {
		return this.right;
	}
	
	public AVLNode parent() {
		return this.parent();
	}

	protected void setHeight() {
		this.height = Math.max(height(left), height(right)) + 1; 
	}
	
	protected void setLeft(AVLNode node) {
		this.left = node; 
	}
	
	protected void setRight(AVLNode node) {
		this.right = node; 
	}
	
	protected void setParent(AVLNode node) {
		this.parent = node;
	}
	
	public int balanceFactor() {
		return height(left) - height(right);
	}
	
}
