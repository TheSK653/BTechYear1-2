package java_pattern_ques;

public class pattern_12 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 5;
		int star = 1;
		int row = 1;
		int space = n-1;
		
		while (row<=n) {
			// space
			int i = 1;
			while (i<=space) {
				System.out.print("  ");
				i++;
			}
			// star
			int j = 1;
			while (j<=star) {
				if (j%2 != 0) {
				System.out.print("* ");
				j++;
				}
				else {
				System.out.print("! ");
				}
			}
			// next row ki prep
			System.out.println();
			row++;
			space--;
			star+=2; //star = star + 2;
			}
		}
	}
