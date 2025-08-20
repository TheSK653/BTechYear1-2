package time_complexity_prob;

public class binary_search {
	public static void main(String[] args) {
        int[] arr = {-1,0,3,5,9,12};
        int item = 5;
        System.out.println(Search(arr, item));
    }

    public static int Search(int[] arr, int item) {
        int low = 0;
        int high = arr.length-1;
        while (low <= high) {
            int mid = (low+high)/2;
            if (arr[mid] == item) {
                return mid;
            }
            else if (arr[mid] > item) {
                high = mid-1;
            }
            else {
                low = mid+1;
            }
        }
        return -1;
    }
}
