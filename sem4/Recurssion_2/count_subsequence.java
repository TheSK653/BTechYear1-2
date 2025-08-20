package Recurssion_2;

public class count_subsequence {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String ques = "abc";
		System.out.println("\n" + Count_sub(ques, ""));
	}
	
	public static int  Count_sub(String ques, String ans) {
		if (ques.length() == 0) {
			System.out.print(ans + " ");
			return 1;
		}
		char ch = ques.charAt(0);
		int a = Count_sub(ques.substring(1), ans);
		int b = Count_sub(ques.substring(1), ans + ch);
		return a + b;
	}
}
