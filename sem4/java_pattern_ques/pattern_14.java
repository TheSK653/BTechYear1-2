package java_pattern_ques;

public class pattern_14 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 5;
		int star = 1;
		int row = 1;
		int space = n-1;
		
		while (row<=space) {
			int j=1;
			while (j<=space) {
				System.out.print("  ");
				j++;
			}
		}
		while (row<= 2*n-1) {
			//star
			int i=1;
			while (i<= star) {
				System.out.print("* ");
				i++;
			}
			//Mirror
			if (row<n) {
				star++;
			} else {
				star--;
			}
			// next row prep
			System.out.println();
			row++;
			}
		}
	}