package DataStructures;

import java.util.Arrays;
import java.util.Iterator;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ConcurrentModificationException;
import java.lang.NoSuchMethodException;

public class Stream<T> implements Iterable<StreamItem<T>>{
	
	private ArrayList<StreamItem<T>> stream;
	
	public Stream() {
		this.stream = new ArrayList<>();
	}
	
	
	public Stream(List<T> list) {
		this();
		for(T item : list) {
			stream.add(new StreamItem<T>(item, 1.0));
		}
	}	
	
	public Stream(T[] array) {
		this(Arrays.asList(array));
	}
	
	public <N extends Number> Stream(Map<T, N> map) {
		this();
		Iterator<Map.Entry<T, N>> iter = map.entrySet().iterator();
		while(iter.hasNext()) {
			Map.Entry<T, N> entry = iter.next();
			stream.add(new StreamItem<T>(entry.getKey(), entry.getValue().doubleValue()));
		}
	}
	
	//delete later
	public void put(StreamItem<T> streamItem) {
		this.stream.add(streamItem);
	}
	
	//delete later
	public void put(T item, int weight) {
		this.put(new StreamItem(item, weight));
	}
	
	public StreamIterator<T> iterator() {
		return new StreamIterator<T>();
	}
	
	public static void main(String[] args) {
		HashMap<String, Integer> map = new HashMap<>();
		map.put("Hi", 2);
		map.put("Bye", 5);
		map.put("Why",-3);
		Integer[] array = {5, 6, 3, 4, 2, 2, 2, 2, 1, 2, 1, 3, 2, 3};
		//ArrayList<Integer> arrayList = new ArrayList<Integer>((ArrayList)Arrays.asList(array));
		Stream<String> stream = new Stream<String>(map); 
		for(StreamItem<String> item : stream) {
			System.out.println(item);
		}
	}
	
	private class StreamIterator<T> implements Iterator<StreamItem<T>> {
		
		private int expectedSize = stream.size();
		private int index;
		
		public boolean hasNext() {
			if(index >= expectedSize) return false;
			return true;
		}
		
		public StreamItem<T> next() {
			if(stream.size() != expectedSize) {
				throw new ConcurrentModificationException();
			} else {
				return (StreamItem<T>)stream.get(index++);
			}
		}
		
		public void remove() {
		}
		
	}

}
