package Hash;

import java.util.Random;

public class TwoUniversal {

	private final int PRIME; 
	private int a, b, m; 
	private Random random; 
	
	public TwoUniversal() {
		this(40127);
	
	}
	
	public TwoUniversal(int m) {
		this.random = new Random();
		this.m = m;
		this.PRIME = generatePrime();
		this.generateHash();
	}
	
	 private static boolean isPrime(long n) {
			if(n < 2) return false;
			if(n == 2 || n == 3) return true;
			if(n%2 == 0 || n%3 == 0) return false;
			long sqrtN = (long) Math.sqrt(n)+1;
			for(long i = 6L; i <= sqrtN; i += 6) {
			    if(n%(i-1) == 0 || n%(i+1) == 0) return false;
			}
		return true;
	 }

	 /* TODO: 
	  * Rewrite this terribly awful way of finding primes
	  */
	 private int findPrime() {
		 return random.nextInt(m) + m;
	 }
	 
	 /* TODO: 
	  * Rewrite this terribly awful way of finding primes
	  */
	 private int generatePrime() {
		 int rand = 0;
		 while(! isPrime(rand)) {
			 rand = findPrime();
		 }
		return rand;
    }

    public void generateHash() {
		this.a = random.nextInt(PRIME-1)+1;
		this.b = random.nextInt(PRIME);
    }

    public <E> int hash(E e) {
    	if(e instanceof Number) {
    		return hashInt((Number) e);
    	}
    	else {
    		return hashInt(e.hashCode());
    	}
    }
    
    public int hashInt(Number x) {
    	//System.out.println("\t\tUsing a = " + a + " and b = " + b + " and p = " + PRIME);
    	int hash = (int)((((a * x.doubleValue()) + b) % PRIME) % m);
		return (hash < 0) ? (hash + m) : hash;	    
	}
    
    public boolean equals(TwoUniversal other) {
    	return (this.a == other.a) && (this.b == other.b) &&
    		   (this.PRIME == other.PRIME) && (this.m == other.m);
    }
    
    public String toString() {
    	return "((((" + this.a + " * x) + " + this.b + ") % " + this.PRIME + ") % " + this.m + ")";
    }
    
    public static void main(String[] args) {
    	TwoUniversal u = new TwoUniversal(2);
    	TwoUniversal v = new TwoUniversal(2);
    	/*u.generateHash();
    	for(int i = 0; i < 100; i++) {
    		System.out.println(u.hash(i));
    	}*/
    	System.out.println(u.equals(v));
    }

}
