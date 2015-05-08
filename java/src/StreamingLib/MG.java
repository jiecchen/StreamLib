package StreamingLib;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import DataStructures.Stream;
import DataStructures.StreamItem;

public class MG<T> extends Sketch<T>{

	private int k;
	private HashMap<T, Integer> A; 
	
	public MG() {
		this.k = 2; 
		this.A = new HashMap<>();
	}
	
	public MG(int k) {
		this();
		this.k = k; 
	}
	
	public void process(StreamItem<T> item) {
		if(A.containsKey(item.item())) {
			A.put(item.item(), A.get(item.item()) + 1);
		} else if(A.size() < k-1) {
			A.put(item.item(), 1);
		} else {
			Iterator<Map.Entry<T, Integer>> iter = A.entrySet().iterator();
			while(iter.hasNext()) {
				Map.Entry<T, Integer> entry = iter.next();
				Integer freq = entry.getValue() - 1;
				if(freq == 0) iter.remove();
				else entry.setValue(freq);
			}
		}
	}

	public int getEstimation(T item) {
		if(A.containsKey(item)) return A.get(item);
		else return 0;
	}

//Not defined for MG: return some error? 
	public Sketch<T> merge(Sketch<T> other) {
		return null;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		MG<Integer> mg = new MG<>(5); 
		Integer[] list = {1, 1, 1, 1, 5, 6, 2, 5, 5, 5, 1, 5, 6, 6, 9, 3};
		Stream<Integer> stream = new Stream<Integer>(list);
		//int[] list = {1, 2, 5, 6, 9};
		mg.batchProcess(stream);
		System.out.println(mg.getEstimation(6));
	}

}
