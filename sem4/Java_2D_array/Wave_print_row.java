package Java_2D_array;

public class Wave_print_row {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] arr = { { 2, 3, 4, 5 },
						{ 1, 8, 9, 7 },
						{ 12, 56, 78, 23 } };
		print(arr);
	}

	public static void print(int[][] arr) {
		for (int row = 0; row < arr.length; row++) {
			if (row % 2 == 0) {
				for (int col = 0; col < arr[row].length; col++) {
					System.out.print(arr[row][col] + " ");
				}
			} else {
				for (int col = arr[row].length - 1; col >= 0; col--) {
					System.out.print(arr[row][col] + " ");
				}
			}
		}

	}

}
