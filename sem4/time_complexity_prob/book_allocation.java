package time_complexity_prob;
import java.util.*;
public class book_allocation {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t-->0) {
			int books = sc.nextInt(); int nos = sc.nextInt(); 
			int[] page = new int[books];
			for (int i=0; i<page.length; i++) {
				page[i] = sc.nextInt();
			}
			System.out.println(Maximum_page(page, nos));
		}
		sc.close();
    }

	public static int Maximum_page(int[] page, int nos) {
		int low = 0; int high = 0; int ans = 0;
		for (int i=0; i<page.length; i++) {
			high = high + page[i];
		}
		while (low<=high) {
			int mid = (low+high)/2;
			if (isitPossible(page, nos, mid) == true) {ans = mid; high = mid - 1;}
			else {low = mid + 1;}
		}
		return ans; 
	}

	public static boolean isitPossible(int[] page, int nos, int mid) {
		int student = 1; int readpage = 0;
		int i = 0;
		while (i<page.length) {
			if (readpage + page[i] <= mid) {readpage+=page[i]; i++;}
			else {student++; readpage = 0;}
			if (student > nos) {return false;} 
		}
		return true; 
	}
}
