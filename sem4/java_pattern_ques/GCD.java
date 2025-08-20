package java_pattern_ques;

public class GCD {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int div = 36;
		int divd = 60;
		while (divd % div!= 0) {
			int rem = divd % div;
			divd = div;
			div = rem;
		}
		System.out.println(div);

	}

}
