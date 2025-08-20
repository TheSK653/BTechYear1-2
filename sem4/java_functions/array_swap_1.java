package java_functions;

public class array_swap_1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[]arr = {2,3,4,1,7,9,8};
		System.out.println(arr[0] + " " + arr[1]);
		Swap(arr[0],arr[1]);
		System.out.println(arr[0] + " " + arr[1]);
	}
	public static void Swap(int a, int b) {
		int c=a;
		a=b;
		b=c;
	}

}
