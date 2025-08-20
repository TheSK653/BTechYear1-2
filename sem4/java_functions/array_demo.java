package java_functions;

import java.util.*;

public class array_demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for (int i=0; i<arr.length; i++ ) {
			arr[i] = sc.nextInt();
		}
		Display(arr);
		sc.close();
	}
	public static void Display(int[] arr) {
		for (int i =0;i<arr.length;i++ ) {
			System.out.print(arr[i] + " ");
		}
	}
}
		
//		int[] num = {1,5,7,3};
//		//System.out.println(arr);
//		System.out.println(num);
//		int[] other = arr;
//		System.out.println(other.length);
//		num[0] = 15;
//		arr[1] = 25;
//		arr[2] = 35;
//		arr[3] = 45;
//		
//		System.out.println(num[0]);

	
	


