package String;

public class check_palindromic {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "mukul";
		System.out.println(isPalindromic(s));

	}

	public static boolean isPalindromic(String s) {
		int i = 0;
		int j = s.length() - 1;
		while (i < j) {
			if (s.charAt(i) != s.charAt(j)) {
				return false;
			}
			i++;
			j--;
		}
		return true;
	}
}
