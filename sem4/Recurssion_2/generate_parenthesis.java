package Recurssion_2;

public class generate_parenthesis {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 3;
//		List<String> l = new ArrayList<>();
		Parentheses(n, 0, 0, "");
//		Parentheses(n, 0, 0, "",l);
//		System.out.println(l);

	}
//	public static void Parentheses(int n, int closed, int open, String ans,List<String> l)
	public static void Parentheses(int n, int closed, int open, String ans) {
		if (open == n && closed == n) {
			System.out.println(ans);
//			ll.add(ans);
			return;
		}
		if (open > n || closed > open) {
			return;
		}

		Parentheses(n, closed, open + 1, ans + "(");     //fifth parameter l(optional)
		Parentheses(n, closed + 1, open, ans + ")");
	}

}
