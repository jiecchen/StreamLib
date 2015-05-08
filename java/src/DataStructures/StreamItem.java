package DataStructures;

import java.util.Iterator;

public class StreamItem<T> {

	private T item;
	private double weight;
	
	public StreamItem(T item, double weight) {
		this.item = item;
		this.weight = weight;
	}
	
	public T item() {
		return this.item;
	}
	
	public double weight() {
		return this.weight;
	}
	
	public String toString() {
		return "(" + item + ", " + weight + ")";
	}

}
