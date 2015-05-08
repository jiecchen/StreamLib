package StreamingLib;

import java.util.ArrayList;
import java.util.Arrays;

import DataStructures.Stream;
import DataStructures.StreamItem;
import Hash.TwoUniversal;

public class CountSketch<T> extends Sketch<T> {

	private double epsilon;
	private int[] C;
	private TwoUniversal h;
	private TwoUniversal g; 
	
	public CountSketch() {
		this.epsilon = 0.01;
	}
	
	public CountSketch(double epsilon) {
		if(epsilon <= 0) {
			throw new IllegalArgumentException("Epsilon must be positive");
		}
		this.epsilon = epsilon;
		int capacity = (int)Math.ceil(3/Math.pow(epsilon, 2));
		this.C = new int[capacity];
		Arrays.fill(C, 0, capacity, 0);
		this.h = new TwoUniversal(capacity);
		this.g = new TwoUniversal(2); //will produce either 0 or 1
	}
	
	public void process(StreamItem<T> item) {
		int gInt = g.hash(item.item());
		gInt = (gInt == 0) ? -1 : gInt;
		int hInt = h.hash(item.item());
		
		C[hInt] = C[hInt] + ((int)item.weight())*gInt ;
	}
	
	public int getEstimation(T t) {
		return ((g.hash(t) == 0) ? -1 : g.hash(t)) * this.C[h.hash(t)];
	}
	
	public Sketch<T> merge(Sketch<T> other) {
		return null;
	}
	
	public static void main(String[] args) {
		CountSketch<String> cs = new CountSketch<>(.5);
		String[] array = {"hi", "hi", "what", "Rachel", "hi", "hi", "Jeremy", "Jeremy", "Jeremy", "there", "there", "Rachel"};
		Stream<String> stream = new Stream<String>(array);
		cs.batchProcess(stream);
		System.out.println(cs.getEstimation("hi")); 

	}

}
