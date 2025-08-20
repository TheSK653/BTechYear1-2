package java_functions;

public class Reverse_Range {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {3,5,1,7,8,6,9,11,15,17,18,16,23};
		Reverse(arr,3,8);
		for (int i=0; i<arr.length; i++) {
			System.out.print(arr[i]+ " ");
		}
	}
	public static void Reverse(int[] arr, int start, int end) {
		while (start < end) {
			int temp = arr[start];
			arr[start] = arr[end];
			arr[end] = temp;
			start++;
			end--;
		}
	}

}
