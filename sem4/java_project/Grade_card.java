package java_project;

public class Grade_card {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n=67;
		
		if (n>=75) {
			System.out.println("A Grade");
		}
		else if (n>=65 && n<75) {
			System.out.println("B Grade");
		}
		else if (n>=55 && n<65) {
			System.out.println("C Grade");
		}
		else if (n>=45 && n<55) {
			System.out.println("D Grade");
		}
		else {
			System.out.println("FAIL");
		}

	}

}
