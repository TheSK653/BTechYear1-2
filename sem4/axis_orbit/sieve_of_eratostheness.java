package axis_orbit;
import java.util.*;
public class sieve_of_eratostheness {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 10;
		System.out.println(PrimeSieve(n));
	}

	// jis index pe 0 hai us index ko prime number bolenge
	public static int PrimeSieve(int n) {
		int[] ans = new int[n];
		ans[0] = ans[1] = 1;
		for (int i = 2; i * i <= ans.length; i++) {
			if (ans[i] == 0) {// i prime hai
				for (int j = 2; i * j < ans.length; j++) {
					ans[i * j] = 1;
				}
			}
		}
		int c=0;
		for (int i = 2; i < ans.length; i++) {
			if(ans[i]==0) {
				c++;
			}
		}
		return c;

	}
}
