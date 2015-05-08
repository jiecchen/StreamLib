package DataStructures;

import java.util.Iterator;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

import java.util.ArrayList;
import java.util.LinkedList; 
import java.util.Arrays;

public class Distribution<K> {

	private double cumm;
	private HashMap<Double, K> dict;
	private Random rand; 
	private ArrayList<Double> index;
	
	public Distribution(List<K> stream) {
		HashMap<K, Double> tempDict = new HashMap<K, Double>();
		for(K key : stream) {
			tempDict.put(key, 1.0);
		}
		
		this.cumm = 0;
		this.index = new ArrayList<>();
		index.add(cumm);
		this.dict = buildDict(tempDict);
		
		this.rand = new Random(); 
		
	}
	
	private HashMap<Double, K> buildDict(HashMap<K, Double> map) {
		HashMap<Double, K> ans = new HashMap<>();
		Iterator<Map.Entry<K, Double>> iter = map.entrySet().iterator();
		while(iter.hasNext()) {
			Map.Entry<K, Double> entry = iter.next();
			ans.put(cumm, entry.getKey());
			cumm += entry.getValue();
			index.add(cumm);
		}
		return ans; 
	}
	
	//NOT DONE!!!
	public K getSampe() {
		double randNum = rand.nextDouble() * cumm;
		int pos = bisectLeft(randNum, index, 0, index.size());
		return null;
	}
	
	private int bisectLeft(double x, ArrayList<Double> list, int left, int right) {
		if((left - right) == 0) return left; 
		int mid = (left + right) / 2; 
		if((left - right) == 0) return left;
		else if(x > list.get(mid)) return bisectLeft(x, list, mid + 1, right);
		else if(x < list.get(mid)) return bisectLeft(x, list, left, mid - 1);
		else return mid;
	}
	
	public static void main(String[] args) {
		/*ArrayList<Integer> list = new ArrayList<>();
		list.add(5);
		list.add(4);
		list.add(3);
		list.add(3);
		list.add(5);
		Distribution<Integer> dist = new Distribution(list); */

	}

}
