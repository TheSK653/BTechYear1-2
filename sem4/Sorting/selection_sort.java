package Sorting;

public class selection_sort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {4,-1,5,3,2,1,7};
		Sort(nums);
		for (int i =0; i<nums.length;i++ ) {
			System.out.println(nums[i]+ " ");
		}
		//System.out.println(min_form_ith_index(nums, 2));
		
	}
	public static void Sort(int[] nums) {
		for (int turn=1; turn<nums.length; turn++) {
			for (int i=0; i<nums.length-1; i++) {
				if (nums[i] > nums[i+1]) {
					int temp = nums[i];
					nums[i] = nums[i+1];
					nums[i+1] = temp;
					}
	            }  
			}
		}
	
//	public static int min_form_ith_index(int[] nums, int i) {
//		int min =i;
//		for(int j=i+1; j<nums.length; j++) {
//			if (nums[j] < nums[min]) = 
//		}
//		
//	}
	

}
