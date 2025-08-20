package time_complexity_prob;

public class majority_element {
	public static void main(String[] args) {
        int[] nums = {3,2,3};
        int n = nums.length;
        int e = nums[0];
        int vote = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] == e) {
                vote++;
            } else {
                vote--;
                if (vote == 0) {
                    e = nums[i];
                    vote = 1;
                }
            }
        }
        System.out.println(e);
    }
}
