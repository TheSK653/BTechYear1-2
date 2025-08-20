package time_complexity_prob;

public class Kth_root {
	public static void main(String[] args) {
        int k = 3;
        int n = 145;
        System.out.println(kth_root(k, n));
    }
    public static int kth_root(int k, int n) {
        int low = 1;
        int high = n;
        int ans = 0;
        while (low <= high) {
            int mid = (low+high)/2;
            if (Math.pow(mid, k) <= n) {
                ans = mid;
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        return ans;
    }
}
