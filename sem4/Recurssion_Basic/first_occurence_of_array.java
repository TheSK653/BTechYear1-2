package Recurssion_Basic;

public class first_occurence_of_array {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = { 2, 3, 4, 6, 4, 3, 7 };
		int item = 3;
		System.out.println(Index(arr, item, 0));

	}

	public static int Index(int[] arr, int item, int i) {
		if (i == arr.length) {
			return -1;
		}
		if (arr[i] == item) {
			return i;
		}
		return Index(arr, item, i + 1);
	}
}
