package Java_2D_array;

public class Gas_station {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] gas = {1,2,3,4,5};
		int[] cost = {3,4,5,1,2};
		System.out.println(canCompleteCircuit(gas, cost));

	}
	public static int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0;
        for (int i=0; i<cost.length; i++) {
            total += gas[i] - cost[i];
        }
        if (total<0) {
            return -1;
        }
        int idx = 0;
        int current = 0;
        for (int i=0; i<cost.length; i++) {
            current += gas[i] - cost[i];
            if (current<0) {
                current = 0;
                idx = i+1;
            }
        }
        return idx;
    }

}
