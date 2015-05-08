/**
 * 
 */
package StreamingLib;

import DataStructures.Stream;
import DataStructures.StreamItem;

/**
 * @author rachellowden
 *
 */

public abstract class Sketch<T> {

	public abstract void process(StreamItem<T> t);
	
	public void batchProcess(Stream<T> s) {
		for(StreamItem<T> t : s) {
			this.process(t);
		}
	}
	
	public abstract int getEstimation(T t);
	
	public abstract Sketch<T> merge(Sketch<T> other);
	
}
