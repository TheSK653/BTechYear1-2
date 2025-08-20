package Recurssion_Basic;
public class power {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 2;
		int n = 7;
		System.out.println(pow(a, n));
	}

	public static int pow(int a, int n) {
		if(n==0) {
			return 1;
		}
		int ans=pow(a, n-1);
		return ans*a;

	}
}
