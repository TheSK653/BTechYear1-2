package time_complexity_prob;
import java.util.*;

public class Rainwater_trapping {
	public static void main(String args[]) {
        Scanner Sc = new Scanner(System.in);
        int t = Sc.nextInt();
        while (t>0) {
            int N = Sc.nextInt();
            int[] arr = new int[N];
            for (int i=0; i<N; i++) {
                arr[i] = Sc.nextInt();
            }
            //left array prefix Max
            int[] left = new int[N];
            left[0] = arr[0]; 
            for (int i=1; i<N; i++) {
                left[i] = Math.max(left[i-1], arr[i]);
            }
            //right array suffix Max
            int[] right = new int[N];
            right[N-1] = arr[N-1];
            for (int i=N-2; i>=0; i--) {
                right[i] = Math.max(right[i+1], arr[i]);
            }
            //Loop time 
            int sum = 0;
            for (int i=0; i<N; i++) {
                sum = sum + Math.min(left[i],right[i]) - arr[i];
            }
            System.out.println(sum);  
            t--; 
        }
        Sc.close();
    }
}
